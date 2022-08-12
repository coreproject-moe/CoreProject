from email.mime import image
from io import BytesIO
from typing import Dict

from apps.api.v1.anime.models import CharacterModel
from core.requests import CachedLimiterSession
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from requests.adapters import HTTPAdapter
from requests_cache import RedisCache
from requests_ratelimiter import RedisBucket
from urllib3.util import Retry
from django.db import IntegrityError

retry_strategy = Retry(
    total=3,
    status_forcelist=[429, 500, 502, 503, 504],
)
adapter = HTTPAdapter(max_retries=retry_strategy)


class Command(BaseCommand):
    help = "Populates the character database from https://jikan.moe"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.session = CachedLimiterSession(
            bucket_class=RedisBucket,
            # Undocumented
            bucket_kwargs={"bucket_name": "jikan_api"},
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

    def get_character_data_from_jikan(self) -> Dict[str, str]:
        res = self.session.get(
            f"https://api.jikan.moe/v4/characters/{self.character_number}"
        )
        data = res.json()

        if (
            res.status_code == 200
            and data.get("status", None) != 404
            and data.get("status", None) != "429"
        ):
            print(f"Got Character Info for {self.character_number}")

            data = data["data"]

        else:
            print(f"Missed info for {self.character_number}")
            data = None

        return data

    def after_populate_anime_characters(self) -> None:
        self.character_number += 1
        if self.character_number > self.character_number_end:
            import sys

            sys.exit(0)

        # Restart Function
        self.populate_anime_characters()

    def populate_anime_characters(self) -> None:
        DATA = self.get_character_data_from_jikan()
        if not DATA:
            self.after_populate_anime_characters()

        try:
            image_url = DATA["images"]["webp"]["image_url"]
        except KeyError:
            image_url = DATA["images"]["jpg"]["image_url"]
        finally:
            character_image = self.session.get(image_url)

        try:
            CharacterModel.objects.create(
                mal_id=self.character_number,
                name=DATA["name"],
                name_kanji=DATA.get("name_kanji", None),
                character_image=ContentFile(
                    BytesIO(character_image.content).read(),
                    f"{self.character_number}.{image_url.split('.')[-1]}",
                ),
                about=DATA["about"],
            )
        except IntegrityError:
            print(f"Entry exists : {self.character_number}")

        finally:
            self.after_populate_anime_characters()

    def handle(self, *args, **options):
        self.character_number = options["character-number-start"]
        self.character_number_end = options["character_number_end"]
        self.populate_anime_characters()
