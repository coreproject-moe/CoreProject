from argparse import ArgumentParser
from io import BytesIO
import os
from typing import Any

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from requests.adapters import HTTPAdapter
from requests_cache import RedisCache  # type: ignore
from requests_ratelimiter import RedisBucket
from urllib3.util import Retry

from apps.staff.models import StaffAlternateNameModel, StaffModel
from core.utilities.CachedLimiterSession import (  # pylint: disable=import-error
    CachedLimiterSession,
)

retry_strategy = Retry(
    total=3,
    status_forcelist=[408, 429, 500, 502, 503, 504],
)
adapter = HTTPAdapter(max_retries=retry_strategy)


class Command(BaseCommand):
    """
    Populates the character database
        How does it achieve this?
        First we are taking `self.staff_number` as a command line argument.
            Then using a while loop :
                1. Requesting the data from `https://api.jikan.moe/v4`
                2. Using the `staff_name` from data(jikan) we are getting `kitsu_id` from kitsu
                3. Using the `staff_name` from data(jikan) we are getting `anilist_id` from anilist
                4. Saving everything to `CharacterModel`
    """

    help = "Populates the people database"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.mal_rate_limit_file_name = "mal_ratelimit.txt"
        self.kitsu_not_found_file_name = "kitsu_not_found.txt"
        self.anilist_not_found_file_name = "anilist_not_found.txt"

        self.staff_number: int
        self.staff_number_end: int

        self.staff_name: str
        self.staff_name_kanji: str
        self.staff_image: BytesIO = BytesIO()

        self.staff_about: str
        self.image_url: str

        # Tried to implement Facade pattern
        self.session = CachedLimiterSession(
            bucket_class=RedisBucket,
            # Undocumented
            bucket_kwargs={"bucket_name": "_populate_"},
            backend=RedisCache(),
            # https://docs.api.jikan.moe/#section/Information/Rate-Limiting
            per_minute=60,
            per_second=1,
            # https://requests-cache.readthedocs.io/en/stable/user_guide/expiration.html
            expire_after=360,
        )

        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "staff-number-start",
            nargs="?",
            type=int,
            default=1,
            help="Specifies the starting number for staff.",
        )
        parser.add_argument(
            "--staff-number-end",
            type=int,
            default=100_000,
            help="Specifies the stopping number for staff.",
        )

    def handle(self, *args: Any, **options: Any) -> None:
        """Starting point for our application"""
        self.staff_number = options["staff-number-start"]
        self.staff_number_end = options["staff_number_end"]
        self.populate_anime_staff()

    def get_staff_data_from_kitsu(
        self,
        staff_number: int,
        session: CachedLimiterSession,
    ) -> str | None:
        res = session.get(f"https://kitsu.io/api/edge/people/{staff_number}")
        data = res.json()
        staff_name = None

        if data:
            try:
                data = data["data"]
                staff_name = data["attributes"]["name"]
            except IndexError:
                pass

        return staff_name

    def get_staff_data_from_anilist(
        self,
        staff_name: str | None,
        session: CachedLimiterSession,
    ) -> str | None:
        """
        :param staff_name: The name of the character
        :param session: Requests instance to get data
        """
        anilist_id = None
        if not staff_name:
            return anilist_id

        query = {
            "query": """
            query (
                $page:Int = 1
                $id:Int
                $search:String
                $isBirthday:Boolean
                $sort:[StaffSort]=[FAVOURITES_DESC]
            ) {
                Page(
                    page:$page,
                    perPage:20
                ) {
                    pageInfo {
                        total
                        perPage
                        currentPage
                        lastPage
                        hasNextPage
                    }
                    staff (
                        id:$id
                        search:$search
                        isBirthday:$isBirthday
                        sort:$sort
                    ) {
                        id name{userPreferred}
                        image{large}
                    }
                }
            }
            """,
            "variables": {
                "page": 1,
                "type": "STAFF",
                "search": staff_name,
                "sort": "SEARCH_MATCH",
            },
        }
        res = session.post(url="https://graphql.anilist.co/", json=query)

        if res.status_code == 200:
            try:
                data = res.json()
                anilist_id = data["data"]["Page"]["staff"][0]["id"]
                # self.stdout.write(f"Got Staff Info for {staff_number} | Anilist")

            except (IndexError, KeyError):
                self.stdout.write(f"Entry for {staff_name} doesn't exist | Anilist")

                # Write the number to a file so that we can deal with it later
                file = open(self.anilist_not_found_file_name, "a", encoding="utf-8")
                file.write(f"{str(staff_name)}\n")
                file.close()

        else:
            pass
            # self.stdout.write(f"Missed info for {staff_number} | Anilist")

        return anilist_id

    def get_staff_data_from_jikan(
        self,
        staff_name: str | None,
        session: CachedLimiterSession,
    ) -> dict[Any, Any] | None:
        """
        :param staff_name: The name of the staff
        :param session: Requests instance to get data
        """
        returnable_data = None
        if not staff_name:
            return returnable_data

        # In jikan staff = people
        res = session.get(
            "https://api.jikan.moe/v4/people",
            params={
                "q": staff_name,
            },
        )
        data = res.json()

        if res.status_code == 200:
            try:
                data = data["data"][0]
                returnable_data = data

            except IndexError:
                pass

        return returnable_data

    def populate_anime_staff(self) -> None:
        """
        Function's purpose :
            1. Request the data from `https://api.jikan.moe/v4`
            2. Using the `staff_name` from data(jikan) get `kitsu_id` from kitsu
            3. Using the `staff_name` from data(jikan) get `anilist_id` from anilist
            4. Save everything to `CharacterModel`
        """

        if self.staff_number == 1:
            # If user starts from 0 remove files which are necessary for logging failed request
            files_to_remove = [
                self.mal_rate_limit_file_name,
                self.anilist_not_found_file_name,
                self.kitsu_not_found_file_name,
            ]
            for file in files_to_remove:
                if os.path.exists(file):
                    os.remove(file)

        while self.staff_number < self.staff_number_end:
            staff_name = self.get_staff_data_from_kitsu(
                staff_number=self.staff_number,
                session=self.session,
            )
            data = self.get_staff_data_from_jikan(
                staff_name=staff_name,
                session=self.session,
            )

            if data:
                try:
                    self.image_url = data["images"]["webp"]["image_url"]
                except KeyError:
                    self.image_url = data["images"]["jpg"]["image_url"]
                finally:
                    image = self.session.get(self.image_url)
                    self.staff_image = BytesIO(image.content)

                try:
                    database, _ = StaffModel.objects.update_or_create(
                        kitsu_id=self.staff_number,
                        name=staff_name,
                        defaults={
                            "mal_id": data.get("mal_id"),
                            "anilist_id": self.get_staff_data_from_anilist(
                                staff_name,
                                session=self.session,
                            ),
                            "given_name": data.get("given_name"),
                            "family_name": data.get("family_name"),
                            "staff_image": ContentFile(
                                self.staff_image.read(),
                                f"{self.staff_number}.{self.image_url.split('.')[-1]}",
                            ),
                            "about": data.get("about"),
                        },
                    )

                    for name in data.get("alternate_names", []):
                        (
                            instance,
                            created,
                        ) = StaffAlternateNameModel.objects.get_or_create(name=name)
                        database.alternate_names.add(instance)
                # Add
                except IntegrityError as e:
                    print(e)
                    self.stdout.write(f"Entry exists : {self.staff_number}")

            self.after_populate_anime_staff()

    def after_populate_anime_staff(self) -> None:
        self.staff_name = ""
        self.staff_name_kanji = ""
        self.staff_about = ""
        self.staff_image.truncate(0)

        self.staff_number += 1
