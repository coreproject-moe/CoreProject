from argparse import ArgumentParser
from datetime import datetime, timedelta
from io import BytesIO
import os
import textwrap
from typing import Any

from django.conf import settings
from django.contrib.humanize.templatetags.humanize import intcomma, naturaltime
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from requests.adapters import HTTPAdapter
from requests_cache import RedisCache  # type: ignore
from requests_ratelimiter import RedisBucket
from urllib3.util import Retry

# pylint: disable=import-error
from apps.staffs.models import StaffAlternateNameModel, StaffModel
from core.utilities.CachedLimiterSession import CachedLimiterSession

retry_strategy = Retry(
    total=settings.MAX_RETRY,
    status_forcelist=settings.REQUEST_STATUS_CODES_TO_RETRY,
)
adapter = HTTPAdapter(max_retries=retry_strategy)


class Command(BaseCommand):
    help = "Populates the staff (people) database"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

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

        # FIles
        self.MAL_RATE_LIMIT_FILE_NAME = "(Staff)_mal_not_found.txt"
        self.KITSU_NOT_FOUND_FILE_NAME = "(Staff)_kitsu_not_found.txt"
        self.CHARACTER_LOCK_FILE_NAME = "(Staff)_anilist_not_found.txt"
        self.STAFF_LOCK_FILE_NAME = "Staff.lock"

        self.staff_number: int
        self.starting_number: int
        self.ending_number = self.get_ending_number()

        self.staff_name: str
        self.staff_name_kanji: str
        self.staff_about: str

        # A list to keep items
        self.success_list: list[str] = []
        self.error_list: list[str] = []
        self.warning_list: list[str] = []

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "-sn",  # Character Number
            "--staff-number-start",
            type=int,
            default=1,
            help="Specifies the starting number for character.",
        )

        parser.add_argument(
            "-wsn",  # While starting number
            "--starting-number",
            type=int,
            default=1,
            help="Specifies the starting number for while loop.",
        )

    def handle(self, *args: Any, **options: Any) -> None:
        """Starting point for our application"""
        self.staff_number = options["staff_number_start"]
        self.starting_number = options["starting_number"]
        self.stdout.write(
            textwrap.dedent(
                f"""

                Starting Number : {
                    self.style.SUCCESS(
                        str(
                            intcomma(
                                self.staff_number
                            )
                        )
                    )
                }
                Total `staff` to get :  {
                    self.style.SUCCESS(
                        str(
                            intcomma(
                                self.ending_number
                            )
                        )
                    )
                }
                Time to finish : {
                    self.style.SUCCESS(
                        str(
                           naturaltime(
                                datetime.now()
                                +
                                timedelta(
                                    minutes=
                                        round(
                                            (
                                                self.ending_number
                                                -
                                                self.staff_number
                                            )
                                            /
                                            settings.MAX_REQUESTS_PER_MINUTE
                                    )
                                )
                           )
                        )
                    )
                }

                """
            )
        )
        self.populate_anime_staff()

    def get_ending_number(self) -> int:
        res = self.session.get("https://kitsu.io/api/edge/people/")
        data = res.json()
        return int(data["meta"]["count"])

    def get_staff_data_from_kitsu(
        self,
        staff_number: int,
        session: CachedLimiterSession,
    ) -> str | None:
        res = session.get(f"https://kitsu.io/api/edge/people/{staff_number}")
        data = res.json()
        staff_name = None

        if res.status_code == 200 and data:
            try:
                data = data["data"]
                staff_name = data["attributes"]["name"]
                self.success_list.append(self.style.SUCCESS("Kitsu"))

            except IndexError:
                self.warning_list.append(self.style.WARNING("Kitsu"))

                # Write the number to a file so that we can deal with it later
                file = open(self.KITSU_NOT_FOUND_FILE_NAME, "a", encoding="utf-8")
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
        res_data = res.json()

        if res.status_code == 200:
            for data in res_data["data"]["Page"]["staff"]:
                # If the Anilist ID exists in database
                # Skip to next iteration
                if StaffModel.objects.filter(anilist_id=data["id"]).exists():
                    continue
                anilist_id = data["id"]
            if anilist_id:
                self.success_list.append(self.style.SUCCESS("Anilist"))
            else:
                self.warning_list.append(self.style.WARNING("Anilist"))

                # Write the number to a file so that we can deal with it later
                file = open(self.CHARACTER_LOCK_FILE_NAME, "a", encoding="utf-8")
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
        res_data = res.json()

        if res.status_code == 200:

            for data in res_data["data"]:
                # If the MyAnimeList ID exists in database
                # Skip to next iteration
                if StaffModel.objects.filter(mal_id=data["mal_id"]).exists():
                    continue

                returnable_data = data

            if returnable_data:
                self.success_list.append(self.style.SUCCESS("Jikan"))

            else:
                self.warning_list.append(self.style.WARNING("Jikan"))
                # Write the number to a file so that we can deal with it later
                file = open(self.MAL_RATE_LIMIT_FILE_NAME, "a", encoding="utf-8")
                file.write(f"{str(self.staff_number)}\n")
                file.close()

        else:
            self.error_list.append(self.style.ERROR("Jikan"))

        return returnable_data

    def populate_anime_staff(self) -> None:
        if self.staff_number == 1:
            # If user starts from 0 remove files
            # which are necessary for logging failed request
            files_to_remove = [
                self.MAL_RATE_LIMIT_FILE_NAME,
                self.CHARACTER_LOCK_FILE_NAME,
                self.KITSU_NOT_FOUND_FILE_NAME,
            ]
            for file in files_to_remove:
                if os.path.exists(file):
                    os.remove(file)

        while self.staff_number < self.ending_number:
            staff_name = self.get_staff_data_from_kitsu(
                staff_number=self.staff_number,
                session=self.session,
            )

            if staff_name:
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
                        # Try to get webp image first
                        # If that fails get jpg image
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

            success_error_warnings = set(
                self.success_list + self.error_list + self.warning_list
            )
            self.stdout.write(
                f"Requested `staff_info` for {self.staff_number}"
                " | "
                f"[{', '.join(success_error_warnings)}]"
            )

            # Cleanup
            self.after_populate_anime_staff()

    def after_populate_anime_staff(self) -> None:
        self.staff_name = ""
        self.staff_name_kanji = ""
        self.staff_about = ""

        self.success_list.clear()
        self.error_list.clear()
        self.warning_list.clear()

        self.staff_number += 1
