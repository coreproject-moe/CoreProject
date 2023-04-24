import sys
from typing import NoReturn

import httpx

from shinobi.parser.character import CharacterParser

from django.core.management.base import BaseCommand

from ...models import CharacterModel


class Command(BaseCommand):
    help = "Django command that gets the Character Information given mal_id"

    def __init__(self, *args, **kwargs) -> None:
        self.client = httpx.Client()
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument(
            "character_number",
            type=int,
            help="The character number to get information for",
        )

    def handle(self, *args, **options) -> NoReturn:
        character_number: int = options["character_number"]
        res = self.client.get(f"https://myanimelist.net/character/{character_number}")

        parser = CharacterParser(res.content)
        data_dictionary = parser.build_dictionary()

        try:
            character_instance = CharacterModel.objects.get(mal_id=character_number)
        except CharacterModel.DoesNotExist:
            self.stdout.write(
                f"No CharacterModel found for {self.style.ERROR(character_number)}"
            )
            sys.exit(1)

        for attr, value in data_dictionary.items():
            if value:
                setattr(character_instance, attr, value)

        character_instance.save()
        self.stdout.write(
            f"Successfully got info for {self.style.SUCCESS(character_number)}"
        )
