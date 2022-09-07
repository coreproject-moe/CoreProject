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
from apps.anime.models import CharacterModel
from core.utilities.CachedLimiterSession import CachedLimiterSession

retry_strategy = Retry(
    total=settings.MAX_RETRY,
    status_forcelist=settings.REQUEST_STATUS_CODES_TO_RETRY,
)
adapter = HTTPAdapter(max_retries=retry_strategy)


class Command(BaseCommand):
    """
    Populates the character database
    How does it achieve this?
    First we are taking `self.character_number` as a command line argument.
    Then using a while loop :
        1. Requesting the data from `https://api.jikan.moe/v4`
        2. Using the `character_name` we are getting `kitsu_id`
        3. Using the `character_name` we are getting `anilist_id`
        4. Saving everything to `CharacterModel`
    """

    help = "Populates the character database"

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
        self.mal_rate_limit_file_name = "(Character)_mal_ratelimit.txt"
        self.kitsu_not_found_file_name = "(Character)_kitsu_not_found.txt"
        self.anilist_not_found_file_name = "(Character)_anilist_not_found.txt"

        self.character_number: int
        self.starting_number: int
        self.ending_number = self.get_ending_number()

        self.character_name: str
        self.character_name_kanji: str
        self.character_image: BytesIO

        self.character_about: str
        self.image_url: str

        # A list to keep items
        self.success_list: list[str] = []
        self.error_list: list[str] = []
        self.warning_list: list[str] = []

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "-cn",
            "--character-number-start",
            type=int,
            default=1,
            help="Specifies the starting number for character.",
        )
        parser.add_argument(
            "-sn",
            "--starting-number",
            type=int,
            default=1,
            help="Specifies the starting number for while loop.",
        )

    def handle(self, *args: Any, **options: Any) -> None:
        """Starting point for our application"""
        self.character_number = options["character_number_start"]
        self.starting_number = options["starting_number"]
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
                Total `characters` to get : {
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
        self.populate_anime_characters()

    def get_ending_number(self) -> int:
        res = self.session.get("https://api.jikan.moe/v4/characters")
        data = res.json()
        return int(data["pagination"]["items"]["total"])

    def get_character_data_from_jikan(
        self,
        character_number: int,
        session: CachedLimiterSession,
    ) -> dict[str, str] | None:
        """
        :param character_number: The id of character
        :param session: Requests instance to get data
        """
        res = session.get(f"https://api.jikan.moe/v4/characters/{character_number}")
        data = res.json()
        returnable_data = None

        if res.status_code == 200 and data.get("status", None) not in [404, 408, "429"]:
            self.success_list.append(self.style.SUCCESS("Jikan"))

            returnable_data = data["data"]
            self.character_name = returnable_data["name"]
            self.character_name_kanji = returnable_data.get("name_kanji", None)
            self.character_about = returnable_data.get("about", None)

            # Try to get webp image first
            # If that fails get jpg image
            try:
                self.image_url = returnable_data["images"]["webp"]["image_url"]
            except KeyError:
                self.image_url = returnable_data["images"]["jpg"]["image_url"]
            finally:
                image = self.session.get(self.image_url)
                self.character_image = BytesIO(image.content)

        elif data.get("status", None) == 408:
            self.warning_list.append(self.style.WARNING("Jikan"))

            # Write the number to a file so that we can deal with it later
            file = open(self.mal_rate_limit_file_name, "a", encoding="utf-8")
            file.write(f"{str(character_number)}\n")
            file.close()

        else:
            self.error_list.append(self.style.ERROR("Jikan"))

        return returnable_data

    def get_character_data_from_kitsu(
        self,
        character_name: str,
        session: CachedLimiterSession,
    ) -> str | None:
        """
        :param character_name: The name of the character
        :param session: Requests instance to get data
        """

        res = session.get(
            "https://kitsu.io/api/edge/characters",
            params={
                "filter[name]": {character_name},
            },
        )
        res_data = res.json()
        kitsu_id = None

        if res.status_code == 200:
            try:
                for data in res_data["data"]:
                    # If the Kitsu ID exists in database
                    # Skip to next iteration
                    if CharacterModel.objects.filter(kitsu_id=data["id"]).exists():
                        continue

                    # Side Effect
                    if not self.character_name_kanji:
                        self.character_name_kanji = data["attributes"]["names"].get("ja_jp")

                    kitsu_id = data["id"]
                self.success_list.append(self.style.SUCCESS("Kitsu"))

            except IndexError:
                self.warning_list.append(self.style.WARNING("Kitsu"))

                # Write the number to a file so that we can deal with it later
                file = open(self.kitsu_not_found_file_name, "a", encoding="utf-8")
                file.write(f"{str(character_name)}\n")
                file.close()

        else:
            self.error_list.append(self.style.ERROR("Kitsu"))

        return kitsu_id

    def get_character_data_from_anilist(
        self,
        character_name: str,
        session: CachedLimiterSession,
    ) -> str | None:
        """
        :param character_name: The name of the character
        :param session: Requests instance to get data
        """
        query = {
            "query": """
            query (
                $page:Int = 1
                $id:Int
                $search:String
                $isBirthday:Boolean
                $sort:[CharacterSort]=[FAVOURITES_DESC]
            ) {
                Page (
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
                    characters (
                        id:$id
                        search:$search
                        isBirthday:$isBirthday
                        sort:$sort
                    ) {
                        id
                        name
                        {userPreferred}
                        image
                        {large}
                    }
                }
            }
            """,
            "variables": {
                "page": 1,
                "type": "CHARACTERS",
                "search": character_name,
                "sort": "SEARCH_MATCH",
            },
        }
        res = session.post(url="https://graphql.anilist.co/", json=query)
        res_data = res.json()
        anilist_id = None

        if res_data and res.status_code == 200:
            try:
                for data in res_data["data"]["Page"]["characters"]:
                    # If the Anilist ID exists in database
                    # Skip to next iteration
                    if CharacterModel.objects.filter(anilist_id=data["id"]).exists():
                        continue

                    anilist_id = data["id"]
                self.success_list.append(self.style.SUCCESS("Anilist"))

            except IndexError:
                self.warning_list.append(self.style.WARNING("Anilist"))

                # Write the number to a file so that we can deal with it later
                file = open(self.anilist_not_found_file_name, "a", encoding="utf-8")
                file.write(f"{str(character_name)}\n")
                file.close()

        else:
            self.error_list.append(self.style.WARNING("Anilist"))

        return anilist_id

    def populate_anime_characters(self) -> None:
        """
        Function's purpose :
            1. Request the data from `https://api.jikan.moe/v4`
            2. Using the `character_name` from data(jikan) get `kitsu_id` from kitsu
            3. Using the `character_name` from data(jikan) get `anilist_id` from anilist
            4. Save everything to `CharacterModel`
        """

        if self.character_number == 1:
            # If user starts from 0 remove files
            # which are necessary for logging failed request
            files_to_remove = [
                self.mal_rate_limit_file_name,
                self.anilist_not_found_file_name,
                self.kitsu_not_found_file_name,
            ]
            for file in files_to_remove:
                if os.path.exists(file):
                    os.remove(file)

        while self.starting_number <= self.ending_number:
            data = self.get_character_data_from_jikan(
                character_number=self.character_number,
                session=self.session,
            )

            if data:
                try:
                    CharacterModel.objects.update_or_create(
                        mal_id=self.character_number,
                        defaults={
                            "kitsu_id": self.get_character_data_from_kitsu(
                                character_name=self.character_name,
                                session=self.session,
                            ),
                            "anilist_id": self.get_character_data_from_anilist(
                                character_name=self.character_name,
                                session=self.session,
                            ),
                            "name": self.character_name,
                            "name_kanji": self.character_name_kanji,
                            "character_image": ContentFile(
                                self.character_image.read(),
                                f"{self.character_number}.{self.image_url.split('.')[-1]}",
                            ),
                            "about": self.character_about,
                        },
                    )

                except IntegrityError as e:
                    print(e)
                    self.stdout.write(f"Entry exists : {self.character_number}")

                # Add 1 to `starting_number` on every successful request
                self.starting_number += 1

            self.stdout.write(
                f"Requested `character_info` for {self.character_number}"
                " | "
                f"""`starting_number` {
                    self.starting_number - 1
                    if data else self.starting_number
                }"""
                " | "
                f"[{', '.join(self.success_list + self.error_list + self.warning_list)}]"
            )
            self.after_populate_anime_characters()

    def after_populate_anime_characters(self) -> None:
        self.character_name = ""
        self.character_name_kanji = ""
        self.character_about = ""
        self.character_image.truncate(0)
        self.image_url = ""

        self.success_list.clear()
        self.error_list.clear()
        self.warning_list.clear()

        self.character_number += 1
