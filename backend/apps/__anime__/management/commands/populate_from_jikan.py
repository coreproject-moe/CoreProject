import os
from io import BytesIO

from apps.api.v1.anime.models import CharacterModel
from core.requests import CachedLimiterSession
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from requests.adapters import HTTPAdapter
from requests_cache import RedisCache
from requests_ratelimiter import RedisBucket
from urllib3.util import Retry

retry_strategy = Retry(
    total=3,
    status_forcelist=[408, 429, 500, 502, 503, 504],
)
adapter = HTTPAdapter(max_retries=retry_strategy)


class Command(BaseCommand):
    help = "Populates the character database from https://jikan.moe"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

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

    def get_character_data_from_jikan(self) -> dict[str, str]:
        res = self.session.get(
            f"https://api.jikan.moe/v4/characters/{self.character_number}"
        )
        data = res.json()

        if (
            res.status_code == 200
            and data.get("status", None) != 404
            and data.get("status", None) != 408
            and data.get("status", None) != "429"
        ):
            print(f"Got Character Info for {self.character_number} | Jikan")
            data = data["data"]
            self.character_name = data["name"]
            self.character_name_kanji = data.get("name_kanji", None)
            self.character_about = data.get("about", None)

            try:
                self.image_url = data["images"]["webp"]["image_url"]
            except KeyError:
                self.image_url = data["images"]["jpg"]["image_url"]
            finally:
                self.character_image = self.session.get(self.image_url)

        elif data.get("status", None) == 408:
            print(f"Mal is Rate-Limiting us | {self.character_number}")

            # Write the number to a file so that we can deal with it later
            f = open("skipped.txt", "a")
            f.write(f"{str(self.character_number)}\n")
            f.close()

            # We need to return None as data
            data = None
        else:
            print(f"Missed info for {self.character_number} | Jikan")
            data = None

        return data

    def get_data_from_kitsu(self) -> None:
        if not self.character_name:
            print(f"Skipping | Kitsu")
            return

        res = self.session.get(
            f"https://kitsu.io/api/edge/characters?filter[name]={self.character_name}"
        )

        data = res.json()
        if res.status_code == 200:
            print(f"Got Character Info for {self.character_number} | Kitsu")

            data = data["data"][0]
            self.kitsu_id = data["id"]
            if not self.character_name_kanji:
                self.character_name_kanji = data["attributes"]["names"]["ja_jp"]

        else:
            print(f"Missed info for {self.character_number} | Kitsu")

    def get_data_from_anilist(self) -> None:
        if not self.character_name:
            print(f"Skipping | Anilist")
            return

        query = {
            "query": "query($page:Int = 1 $id:Int $search:String $isBirthday:Boolean $sort:[CharacterSort]=[FAVOURITES_DESC]){Page(page:$page,perPage:20){pageInfo{total perPage currentPage lastPage hasNextPage}characters(id:$id search:$search isBirthday:$isBirthday sort:$sort){id name{userPreferred}image{large}}}}",
            "variables": {
                "page": 1,
                "type": "CHARACTERS",
                "search": self.character_name,
                "sort": "SEARCH_MATCH",
            },
        }
        res = self.session.post(url="https://graphql.anilist.co/", json=query)
        data = res.json()["data"]

        if data and res.status_code == 200:
            try:
                print(f"Got Character Info for {self.character_number} | Anilist")
                self.anilist_id = data["Page"]["characters"][0]["id"]

            except IndexError:
                print(f"Entry for {self.character_name} doesn't exist | Anilist")

                # Write the number to a file so that we can deal with it later
                f = open("anilist.txt", "a")
                f.write(f"{str(self.character_name)}\n")
                f.close()

        else:
            print(f"Missed info for {self.character_number} | Anilist")

    def populate_anime_characters(self) -> None:
        if self.character_number == 1:
            # Remove files which will be necessary for logging failed request
            os.path.exists("skipped.txt") and os.remove("skipped.txt")
            os.path.exists("anilist.txt") and os.remove("anilist.txt")

        while self.character_number < self.character_number_end:
            DATA = self.get_character_data_from_jikan()
            if not DATA:
                self.after_populate_anime_characters()
                continue

            try:
                database = CharacterModel.objects.create(
                    mal_id=self.character_number,
                    name=self.character_name,
                    name_kanji=self.character_name_kanji,
                    character_image=ContentFile(
                        BytesIO(self.character_image.content).read(),
                        f"{self.character_number}.{self.image_url.split('.')[-1]}",
                    ),
                    about=self.character_about,
                )
                # Lazy query
                self.get_data_from_kitsu()
                self.get_data_from_anilist()

                database.kitsu_id = self.kitsu_id
                database.anilist_id = self.anilist_id

                database.save()
            except IntegrityError:
                print(f"Entry exists : {self.character_number}")

            self.after_populate_anime_characters()

    def after_populate_anime_characters(self) -> None:
        self.kitsu_id = None
        self.anilist_id = None

        self.character_name = None
        self.character_name_kanji = None
        self.chatacter_about = None
        self.character_image = None

        self.character_number += 1

    def handle(self, *args, **options):
        self.character_number = options["character-number-start"]
        self.character_number_end = options["character_number_end"]
        self.populate_anime_characters()
