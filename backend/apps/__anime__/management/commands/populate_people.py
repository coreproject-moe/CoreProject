from io import BytesIO
import os

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from requests.adapters import HTTPAdapter
from requests_cache import RedisCache
from requests_ratelimiter import RedisBucket
from urllib3.util import Retry

from apps.api.v1.anime.models import CharacterModel  # pylint: disable=import-error
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

    help = "Populates the character database"

    def __init__(self, *args, **kwargs) -> None:
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

    def add_arguments(self, parser):
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

    def handle(self, *args, **options) -> None:
        """Starting point for our application"""
        self.staff_number = options["staff-number-start"]
        self.staff_number_end = options["staff_number_end"]
        self.populate_anime_staff()

    # Finished
    def get_data_from_anilist(
        self,
        staff_name: str,
        staff_number: int,
        session: CachedLimiterSession,
    ) -> str | None:
        """
        :param staff_name: The name of the character
        :param staff_number: The id of character
        :param session: Requests instance to get data
        """

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
            }""",
            "variables": {
                "page": 1,
                "type": "STAFF",
                "search": {staff_name},
                "sort": "SEARCH_MATCH",
            },
        }
        res = session.post(url="https://graphql.anilist.co/", json=query)
        data = res.json()
        anilist_id = None

        if data and res.status_code == 200:
            try:
                anilist_id = data["data"]["Page"]["characters"][0]["id"]
                self.stdout.write(f"Got Staff Info for {staff_number} | Anilist")

            except IndexError:
                self.stdout.write(f"Entry for {staff_name} doesn't exist | Anilist")

                # Write the number to a file so that we can deal with it later
                file = open(self.anilist_not_found_file_name, "a", encoding="utf-8")
                file.write(f"{str(staff_name)}\n")
                file.close()

        else:
            self.stdout.write(f"Missed info for {staff_number} | Anilist")

        return anilist_id

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
            data = self.get_character_data_from_jikan(
                self.staff_number,
                session=self.session,
            )

            if data:
                try:
                    pass
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
