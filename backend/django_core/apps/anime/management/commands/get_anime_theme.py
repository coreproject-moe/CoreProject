import sys
from typing import NoReturn

from django.core.management.base import BaseCommand

from shinobi.parser.genre import AnimeGenreParser
from shinobi.utilities.session import session

from ...models.anime_theme import AnimeThemeModel


class Command(BaseCommand):
    """
    Uses : AnimeGenreParser ( because both theme and genre are the same urls )
    """

    help = "Django command that gets the Anime Theme Information given mal_id"

    def __init__(self, *args, **kwargs) -> None:
        self.client = session
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument(
            "theme_id",
            type=int,
            help="The Theme ID number to get information for",
        )

    def handle(self, *args, **options) -> NoReturn:
        theme_id: str = str(options["theme_id"])
        res = self.client.get(f"https://myanimelist.net/anime/genre/{theme_id}")

        parser = AnimeGenreParser(res.text)
        data_dictionary = parser.build_dictionary()

        try:
            theme_instance = AnimeThemeModel.objects.get(mal_id=theme_id)
        except AnimeThemeModel.DoesNotExist:
            self.stdout.write(f"No ThemeModel found for {self.style.ERROR(theme_id)}")
            sys.exit(1)

        for attr, value in data_dictionary.items():
            if value:
                setattr(theme_instance, attr, value)

        theme_instance.save()
        self.stdout.write(f"Successfully got info for {self.style.SUCCESS(theme_id)}")
