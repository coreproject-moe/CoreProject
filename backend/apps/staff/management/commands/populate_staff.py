from argparse import ArgumentParser
from io import BytesIO
import os
from typing import Any

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from requests.adapters import HTTPAdapter
from requests_cache import RedisCache  # type: ignore
from requests_ratelimiter import RedisBucket
from urllib3.util import Retry

# pylint: disable=import-error
from apps.staff.models import StaffAlternateNameModel, StaffModel
from core.utilities.CachedLimiterSession import CachedLimiterSession

retry_strategy = Retry(
    total=settings.MAX_RETRY,
    status_forcelist=settings.REQUEST_STATUS_CODES_TO_RETRY,
)
adapter = HTTPAdapter(max_retries=retry_strategy)


class Command(BaseCommand):
    help = "Populates the staff(people) database"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.mal_not_found_file_name = "(Staff)_mal_not_found.txt"
        self.kitsu_not_found_file_name = "(Staff)_kitsu_not_found.txt"
        self.anilist_not_found_file_name = "(Staff)_anilist_not_found.txt"

        self.staff_number: int
        self.staff_number_end: int

        self.staff_name: str
        self.staff_name_kanji: str

        self.staff_about: str
        self.image_url: str

        # Tried to implement Facade pattern
        self.session = CachedLimiterSession(
            bucket_class=RedisBucket,
            backend=RedisCache(),
            # Undocumented ( pyrate-limiter )
            bucket_kwargs={"bucket_name": settings.BUCKET_NAME},
            # https://docs.api.jikan.moe/#section/Information/Rate-Limiting
            per_minute=settings.MAX_REQUESTS_PER_MINUTE,
            per_second=1,
            # https://requests-cache.readthedocs.io/en/stable/user_guide/expiration.html
            expire_after=360,
        )

        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

        # A list to keep items
        self.success_list: list[str] = []
        self.error_list: list[str] = []
        self.warning_list: list[str] = []

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
                self.success_list.append(self.style.SUCCESS("Kitsu"))

            except IndexError:
                self.warning_list.append(self.style.WARNING("Kitsu"))

                # Write the number to a file so that we can deal with it later
                file = open(self.kitsu_not_found_file_name, "a", encoding="utf-8")
                file.write(f"{str(staff_number)}\n")
                file.close()

        else:
            self.error_list.append(self.style.ERROR("Kitsu"))

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
                self.success_list.append(self.style.SUCCESS("Anilist"))

            except (IndexError, KeyError):
                self.warning_list.append(self.style.WARNING("Anilist"))

                # Write the number to a file so that we can deal with it later
                file = open(self.anilist_not_found_file_name, "a", encoding="utf-8")
                file.write(f"{str(self.staff_number)}\n")
                file.close()

        else:
            self.error_list.append(self.style.WARNING("Anilist"))

        return anilist_id

    def get_staff_data_from_jikan(
        self,
        staff_name: str | None,
        session: CachedLimiterSession,
    ) -> dict[Any, Any]:
        """
        :param staff_name: The name of the staff
        :param session: Requests instance to get data
        """
        returnable_data: dict[Any, Any] = {}
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
                self.success_list.append(self.style.SUCCESS("Jikan"))

            except IndexError:
                self.warning_list.append(self.style.WARNING("Jikan"))
                # Write the number to a file so that we can deal with it later
                file = open(self.mal_not_found_file_name, "a", encoding="utf-8")
                file.write(f"{str(self.staff_number)}\n")
                file.close()

        else:
            self.error_list.append(self.style.ERROR("Jikan"))

        return returnable_data

    def populate_anime_staff(self) -> None:
        if self.staff_number == 1:
            # If user starts from 0 remove files which are necessary for logging failed request
            files_to_remove = [
                self.mal_not_found_file_name,
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

            try:
                (database, _) = StaffModel.objects.update_or_create(
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
                        "about": data.get("about"),
                    },
                )

                if data:
                    try:
                        image_url = data["images"]["webp"]["image_url"]
                    except KeyError:
                        image_url = data["images"]["jpg"]["image_url"]
                    finally:
                        image = self.session.get(image_url)

                        database.staff_image.save(
                            f"{self.staff_number}.{image_url.split('.')[-1]}",
                            ContentFile(
                                BytesIO(image.content).read(),
                            ),
                        )
                        database.save()

                for name in data.get("alternate_names", []):
                    (
                        instance,
                        _,
                    ) = StaffAlternateNameModel.objects.get_or_create(name=name)
                    database.alternate_names.add(instance)

            except IntegrityError as e:
                print(e)
                self.stdout.write(f"Entry exists : {self.staff_number}")

            finally:
                success_error_warnings = (
                    self.success_list + self.error_list + self.warning_list
                )
                self.stdout.write(
                    f"Requested `staff_info` for {self.staff_number} | [{', '.join(success_error_warnings)}]"
                )
                self.after_populate_anime_staff()

    def after_populate_anime_staff(self) -> None:
        self.staff_name = ""
        self.staff_name_kanji = ""
        self.staff_about = ""

        self.success_list.clear()
        self.error_list.clear()
        self.warning_list.clear()

        self.staff_number += 1
