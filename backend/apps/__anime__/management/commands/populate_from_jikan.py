from django.core.management.base import BaseCommand
from apps.api.v1.anime.models import (
    AnimeGenreModel,
    AnimeModel,
    AnimeSynonymModel,
    AnimeThemeModel,
    CharacterModel,
    ProducerModel,
    StudioModel,
)
from core.requests import CachedLimiterSession
from urllib3.util import Retry
from requests_cache import RedisCache
from requests_ratelimiter import RedisBucket
from requests.adapters import HTTPAdapter
from django.core.files.base import ContentFile
from io import BytesIO

retry_strategy = Retry(
    total=3,
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=["OPTIONS"],
)
adapter = HTTPAdapter(max_retries=retry_strategy)


class Command(BaseCommand):
    help = "Populates the database from https://jikan.moe"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.character_number = 1

        self.session = CachedLimiterSession(
            bucket_class=RedisBucket,
            # Undocumented
            bucket_kwargs={"bucket_name": "jikan_api"},
            backend=RedisCache(),
            # https://docs.api.jikan.moe/#section/Information/Rate-Limiting
            per_minute=55,
            per_second=1,
        )
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def populate_anime_characters(self) -> None:
        res = self.session.get(
            f"https://api.jikan.moe/v4/characters/{self.character_number}"
        )
        data = res.json()

        if (
            res.status_code == 200
            and data.get("status", None) != 404
            and data.get("status", None) != "429"
        ):
            print(f"Got Info for {self.character_number}")
            DATA = data["data"]

            try:
                image_url = DATA["images"]["webp"]["image_url"]
            except KeyError:
                image_url = DATA["images"]["jpg"]["image_url"]
            finally:
                character_image = self.session.get(image_url)

            CharacterModel.objects.create(
                mal_id=self.character_number,
                name=DATA["name"],
                name_kanji=DATA["name_kanji"],
                character_image=ContentFile(
                    BytesIO(character_image.content).read(),
                    f"{self.character_number}.{image_url.split('.')[-1]}",
                ),
                about=DATA["about"],
            )
        else:
            print(f"Missed info for {self.character_number}")

        self.character_number += 1

        # We are taking 60,000 characters
        if self.character_number > 60_000:
            import sys

            sys.exit(0)

        # Restart Function
        self.populate_anime_characters()

    def handle(self, *args, **options):
        self.populate_anime_characters()
