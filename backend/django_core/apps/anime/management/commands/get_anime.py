import sys
from typing import NoReturn

from apps.characters.models import CharacterModel
from apps.producers.models import ProducerModel
from apps.staffs.models import StaffModel

from shinobi.parser.anime import AnimeParser
from shinobi.utilities.session import session

from django.core.management.base import BaseCommand

from ...models import AnimeModel, AnimeNameSynonymModel
from ...models.anime_genre import AnimeGenreModel
from ...models.anime_theme import AnimeThemeModel
from ...tasks import get_periodic_anime


class Command(BaseCommand):
    """
    Uses : AnimeGenreParser ( because both theme and genre are the same urls )
    """

    help = "Django command that gets the Anime Information given mal_id"

    def __init__(self, *args, **kwargs) -> None:
        self.client = session
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument(
            "anime_id",
            type=int,
            help="The Theme ID number to get information for",
        )
        parser.add_argument(
            "--create",
            action="store_true",
            help="Flag to indicate that the anime will be created",
        )
        parser.add_argument(
            "--periodic",
            action="store_true",
            help="Flag to periodic task will be created",
        )

    def handle(self, *args, **options) -> NoReturn:
        periodic: bool = options.get("periodic")
        if periodic:
            get_periodic_anime.delay()
            self.stdout.write(f"Successfully stated preiodic celery commands")
            sys.exit(0)

        anime_id: int = options["anime_id"]
        if not anime_id:
            self.stdout.write(self.style.ERROR("No anime_id provided"))
            sys.exit(1)

        create: bool = options.get("create")
        if create:
            anime_instance, _ = AnimeModel.objects.get_or_create(mal_id=anime_id)

        else:
            try:
                anime_instance = AnimeModel.objects.get(mal_id=anime_id)
            except AnimeModel.DoesNotExist:
                self.stdout.write(f"No AnimeModel found for {self.style.ERROR(anime_id)}")
                sys.exit(1)

        res = self.client.get(f"https://myanimelist.net/anime/{anime_id}/")

        parser = AnimeParser(res.text)
        data_dictionary = {k: v for k, v in parser.build_dictionary().items() if v}

        if alternate_name := data_dictionary.pop("name_synonyms"):
            for name in alternate_name:
                (
                    alternate_name_synonym_instance,
                    _,
                ) = AnimeNameSynonymModel.objects.get_or_create(name=name)
                anime_instance.name_synonyms.add(alternate_name_synonym_instance)

        if genres := data_dictionary.pop("genres"):
            for genre in genres:
                anime_genre_instance = AnimeGenreModel.objects.get(mal_id=genre)
                anime_instance.genres.add(anime_genre_instance)

        if themes := data_dictionary.pop("themes"):
            for theme in themes:
                anime_theme_instance = AnimeThemeModel.objects.get(mal_id=theme)
                anime_instance.themes.add(anime_theme_instance)

        if characters := data_dictionary.pop("characters"):
            for character in characters:
                character_instance = CharacterModel.objects.get(mal_id=character)
                anime_instance.characters.add(character_instance)

        if studios := data_dictionary.pop("studios"):
            for studio in studios:
                studio_instance = ProducerModel.objects.get(mal_id=studio)
                anime_instance.studios.add(studio_instance)

        if producers := data_dictionary.pop("producers"):
            for producer in producers:
                producer_instance = ProducerModel.objects.get(mal_id=producer)
                anime_instance.producers.add(producer_instance)

        if staffs := data_dictionary.pop("staffs"):
            for staff in staffs:
                staff_instance = StaffModel.objects.get(mal_id=staff)
                anime_instance.staffs.add(staff_instance)

        # Handle this later :)
        data_dictionary.pop("openings")
        data_dictionary.pop("endings")

        for attr, value in data_dictionary.items():
            setattr(anime_instance, attr, value)

        anime_instance.save()
        self.stdout.write(f"Successfully got info for {self.style.SUCCESS(anime_id)}")
