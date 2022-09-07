from argparse import ArgumentParser
from datetime import datetime, timedelta
from io import BytesIO
import sys
import os
import textwrap
from threading import Event, Thread
from typing import Any

from django.core.management.color import color_style
from django.conf import settings
from django.contrib.humanize.templatetags.humanize import intcomma, naturaltime
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, OutputWrapper
from django.db import IntegrityError
from requests.adapters import HTTPAdapter
from requests_cache import RedisCache  # type: ignore
from requests_ratelimiter import RedisBucket
from urllib3.util import Retry

# pylint: disable=import-error
from apps.anime.models import CharacterModel
from core.utilities.CachedLimiterSession import CachedLimiterSession

retry_strategy = Retry(
    total=settings.MAX_RETRY,
    status_forcelist=settings.REQUEST_STATUS_CODES_TO_RETRY,
)
adapter = HTTPAdapter(max_retries=retry_strategy)


class MyAnimeList(Thread):
    API_URL = "https://api.jikan.moe/v4/characters/"
    MAL_RATE_LIMIT_FILE_NAME = "(Character)_mal_ratelimit.txt"

    # https://docs.api.jikan.moe/#section/Information/Rate-Limiting
    RATE_LIMIT = 60

    def __init__(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            *args,
            **kwargs,
        )

        self.session = CachedLimiterSession(
            bucket_class=RedisBucket,
            backend=RedisCache(),
            # Undocumented ( pyrate-limiter )
            bucket_kwargs={"bucket_name": settings.BUCKET_NAME},
            per_minute=self.RATE_LIMIT,
            per_second=1,
            # https://requests-cache.readthedocs.io/en/stable/user_guide/expiration.html
            expire_after=360,
        )

        self._stop = Event()
        # Borrowed from django
        self.stdout = OutputWrapper(sys.stdout)
        self.style = color_style()

        # Control these to get values
        self.character_number = 1
        self.starting_number = 1
        self.ending_number = self.get_ending_number()

        # A list to keep items
        self.success_list: list[str] = []
        self.error_list: list[str] = []
        self.warning_list: list[str] = []

        # Print infos to stdout
        self.print_stats()

    def print_stats(self) -> None:
        self.stdout.write(
            textwrap.dedent(
                f"""
                Starting Number : {
                    self.style.SUCCESS(
                        str(
                            intcomma(
                                self.character_number
                            )
                        )
                    )
                }
                Total `characters` to get from `jikan` : {
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
                                                self.character_number
                                            )
                                            /
                                            self.RATE_LIMIT
                                    )
                                )
                           )
                        )
                    )
                }
                """
            )
        )

    def get_ending_number(self) -> int:
        res = self.session.get(self.API_URL)
        data = res.json()
        return int(data["pagination"]["items"]["total"])

    def get_data(self) -> dict[Any, Any] | None:
        returnable_data = None

        res = self.session.get(self.API_URL + str(self.character_number))
        data = res.json()

        if res.status_code == 200 and data.get("status", None) not in [404, 408, "429"]:
            self.success_list.append(self.style.SUCCESS("Jikan"))
            returnable_data = data["data"]

        elif data.get("status", None) == 408:
            self.warning_list.append(self.style.WARNING("Jikan"))

            # Write the number to a file so that we can deal with it later
            file = open(self.MAL_RATE_LIMIT_FILE_NAME, "a", encoding="utf-8")
            file.write(f"{str(self.character_number)}\n")
            file.close()

        else:
            self.error_list.append(self.style.ERROR("Jikan"))

        return returnable_data

    def save_items_to_database(
        self,
        character_name: str,
        character_name_kanji: str,
        character_about: str,
        character_image: BytesIO,
        character_image_file_name: str,
    ) -> None:
        # We are matching for unique `character_name`
        CharacterModel.objects.update_or_create(
            name=character_name,
            defaults={
                "mal_id": self.character_number,
                "name_kanji": character_name_kanji,
                "character_image": ContentFile(
                    character_image.read(), character_image_file_name
                ),
                "about": character_about,
            },
        )

    def run(self) -> None:
        # Remove the logging files is starting point is 1
        if self.character_number == 1:
            if os.path.exists(
                self.MAL_RATE_LIMIT_FILE_NAME,
            ):
                os.remove(
                    self.MAL_RATE_LIMIT_FILE_NAME,
                )

        while self.starting_number <= self.ending_number and not self._stop:
            data = self.get_data()

            success_error_warnings = self.success_list + self.error_list + self.warning_list
            self.stdout.write(
                f"Requested `character_info` for {self.character_number}"
                " | "
                f"[{', '.join(success_error_warnings)}]"
            )

            if data:
                character_name = data["name"]
                character_name_kanji = data.get("name_kanji", None)
                character_about = data.get("about", None)

                # Try to get webp image first
                # If that fails get jpg image
                try:
                    image_url = data["images"]["webp"]["image_url"]
                except KeyError:
                    image_url = data["images"]["jpg"]["image_url"]
                finally:
                    image = self.session.get(image_url)

                character_image = BytesIO(image.content)
                file_name = f"{self.character_number}.{image_url.split('.')[-1]}"

                self.save_items_to_database(
                    character_name=character_name,
                    character_name_kanji=character_name_kanji,
                    character_about=character_about,
                    character_image=character_image,
                    character_image_file_name=file_name,
                )

                self.starting_number += 1

            # Clear lists
            self.success_list.clear()
            self.error_list.clear()
            self.warning_list.clear()

            self.character_number += 1


class Command(BaseCommand):
    """Populates the character database"""

    help = "Populates the character database"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def handle(self, *args: Any, **options: Any) -> None:
        """Starting point for our application"""
        mal = MyAnimeList()

        try:
            mal.start()
            mal.join()

        except KeyboardInterrupt:
            
