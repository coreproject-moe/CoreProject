import sys
from typing import NoReturn

import httpx

from shinobi.parser.anime import AnimeParser

from django.core.management.base import BaseCommand

from ...models import AnimeModel


class Command(BaseCommand):
    """
    Uses : AnimeGenreParser ( because both theme and genre are the same urls )
    """

    help = "Django command that gets the Anime Information given mal_id"

    def __init__(self, *args, **kwargs) -> None:
        self.client = httpx.Client()
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument(
            "anime_id",
            type=int,
            help="The Theme ID number to get information for",
        )

    def handle(self, *args, **options) -> NoReturn:
        anime_id: int = options["theme_id"]
        res = self.client.get(f"https://myanimelist.net/anime/{anime_id}/")

        parser = AnimeParser(res.content)
        data_dictionary = parser.build_dictionary()

        try:
            anime_instance = AnimeModel.objects.get(mal_id=anime_id)
        except AnimeModel.DoesNotExist:
            self.stdout.write(f"No ThemeModel found for {self.style.ERROR(theme_id)}")
            sys.exit(1)

        for attr, value in data_dictionary.items():
            if value:
                setattr(anime_instance, attr, value)

        anime_instance.save()
        self.stdout.write(f"Successfully got info for {self.style.SUCCESS(anime_id)}")
