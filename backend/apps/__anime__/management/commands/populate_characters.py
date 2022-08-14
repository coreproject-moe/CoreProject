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
from core.requests import CachedLimiterSession  # pylint: disable=import-error

retry_strategy = Retry(
    total=3,
    status_forcelist=[408, 429, 500, 502, 503, 504],
)
adapter = HTTPAdapter(max_retries=retry_strategy)


class Command(BaseCommand):
    """
    Populates the character database
        How does it achieve this?
        First we are taking `self.character_number` as a command line argument.
            Then using a while loop :
                1. Requesting the data from `https://api.jikan.moe/v4`
                2. Using the `character_name` from data(jikan) we are getting `kitsu_id` from kitsu
                3. Using the `character_name` from data(jikan) we are getting `anilist_id` from anilist
                4. Saving everything to `CharacterModel`
    """

    help = "Populates the character database"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.mal_rate_limit_file_name = "mal_ratelimit.txt"
        self.kitsu_not_found_file_name = "kitsu_not_found.txt"
        self.anilist_not_found_file_name = "anilist_not_found.txt"

        self.character_number: int
        self.character_number_end: int

        self.character_name: str
        self.character_name_kanji: str
        self.character_image: BytesIO = BytesIO()

        self.character_about: str
        self.image_url: str

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
            "character-number-start",
            nargs="?",
            type=int,
            default=1,
            help="Specifies the starting number for character.",
        )
        parser.add_argument(
            "--character-number-end",
            type=int,
            default=100_000,
            help="Specifies the stopping number for character.",
        )

    def handle(self, *args, **options) -> None:
        """Starting point for our application"""
        self.character_number = options["character-number-start"]
        self.character_number_end = options["character_number_end"]
        self.populate_anime_characters()

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
        return_data = None

        if res.status_code == 200 and data.get("status", None) not in [404, 408, "429"]:
            self.stdout.write(f"Got Character Info for {character_number} | Jikan")
            data = data["data"]
            self.character_name = data["name"]
            self.character_name_kanji = data.get("name_kanji", None)
            self.character_about = data.get("about", None)

            try:
                self.image_url = data["images"]["webp"]["image_url"]
            except KeyError:
                self.image_url = data["images"]["jpg"]["image_url"]
            finally:
                image = self.session.get(self.image_url)
                self.character_image = BytesIO(image.content)
                return_data = data

        elif data.get("status", None) == 408:
            self.stdout.write(f"Mal is Rate-Limiting us | {character_number}")

            # Write the number to a file so that we can deal with it later
            file = open(self.mal_rate_limit_file_name, "a", encoding="utf-8")
            file.write(f"{str(character_number)}\n")
            file.close()

        else:
            self.stdout.write(f"Missed info for {character_number} | Jikan")

        return return_data

    def get_data_from_kitsu(
        self,
        character_name: str,
        character_number: int,
        session: CachedLimiterSession,
    ) -> str | None:
        """
        :param character_name: The name of the character
        :param character_number: The id of character
        :param session: Requests instance to get data
        """

        res = session.get(
            f"https://kitsu.io/api/edge/characters?filter[name]={character_name}"
        )
        data = res.json()
        kitsu_id = None

        if res.status_code == 200:
            try:
                data = data["data"][0]

                # Side Effect
                if not self.character_name_kanji:
                    self.character_name_kanji = data["attributes"]["names"]["ja_jp"]

                kitsu_id = data["id"]
                self.stdout.write(f"Got Character Info for {character_number} | Kitsu")

            except IndexError:
                self.stdout.write(f"Entry for {character_name} doesn't exist | Kitsu")

                # Write the number to a file so that we can deal with it later
                file = open(self.kitsu_not_found_file_name, "a", encoding="utf-8")
                file.write(f"{str(character_name)}\n")
                file.close()

        else:
            self.stdout.write(f"Missed info for {character_number} | Kitsu")

        return kitsu_id

    def get_data_from_anilist(
        self,
        character_name: str,
        character_number: int,
        session: CachedLimiterSession,
    ) -> str | None:
        """
        :param character_name: The name of the character
        :param character_number: The id of character
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
                Page(page:$page,perPage:20){
                    pageInfo{
                        total
                        perPage
                        currentPage
                        lastPage
                        hasNextPage
                    }
                    characters(id:$id search:$search isBirthday:$isBirthday sort:$sort){
                        id
                        name
                        {userPreferred}
                        image
                        {large}
                    }
                }
            }""",
            "variables": {
                "page": 1,
                "type": "CHARACTERS",
                "search": character_name,
                "sort": "SEARCH_MATCH",
            },
        }
        res = session.post(url="https://graphql.anilist.co/", json=query)
        data = res.json()
        anilist_id = None

        if data and res.status_code == 200:
            try:
                anilist_id = data["data"]["Page"]["characters"][0]["id"]
                self.stdout.write(
                    f"Got Character Info for {character_number} | Anilist"
                )

            except IndexError:
                self.stdout.write(f"Entry for {character_name} doesn't exist | Anilist")

                # Write the number to a file so that we can deal with it later
                file = open(self.anilist_not_found_file_name, "a", encoding="utf-8")
                file.write(f"{str(character_name)}\n")
                file.close()

        else:
            self.stdout.write(f"Missed info for {character_number} | Anilist")

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
            # If user starts from 0 remove files which are necessary for logging failed request
            files_to_remove = [
                self.mal_rate_limit_file_name,
                self.anilist_not_found_file_name,
                self.kitsu_not_found_file_name,
            ]
            for file in files_to_remove:
                if os.path.exists(file):
                    os.remove(file)

        while self.character_number < self.character_number_end:
            data = self.get_character_data_from_jikan(
                self.character_number,
                session=self.session,
            )

            if data:
                try:
                    CharacterModel.objects.update_or_create(
                        mal_id=self.character_number,
                        defaults={
                            "kitsu_id": self.get_data_from_kitsu(
                                self.character_name,
                                self.character_number,
                                self.session,
                            ),
                            "anilist_id": self.get_data_from_anilist(
                                self.character_name,
                                self.character_number,
                                self.session,
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
                    print(
                        self.get_data_from_anilist(
                            self.character_name,
                            self.character_number,
                            self.session,
                        )
                    )
                    self.stdout.write(f"Entry exists : {self.character_number}")

            self.after_populate_anime_characters()

    def after_populate_anime_characters(self) -> None:
        self.character_name = ""
        self.character_name_kanji = ""
        self.character_about = ""
        self.character_image.truncate(0)

        self.character_number += 1
