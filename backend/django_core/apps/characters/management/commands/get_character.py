import sys
from argparse import ArgumentParser

from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand

from shinobi.parser.character import CharacterParser
from shinobi.utilities.session import session

from ...models import CharacterModel
from ...tasks import get_periodic_character


class Command(BaseCommand):
    help = "Django command that gets the Character Information given mal_id"

    def __init__(self, *args, **kwargs) -> None:
        self.client = session
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "character_id",
            type=int,
            help="The character number to get information for",
            nargs="?",
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

    def handle(self, *args, **options) -> None:
        periodic: bool = options["periodic"]
        if periodic:
            get_periodic_character.delay()
            self.stdout.write("Successfully stated preiodic celery commands")
            sys.exit(0)

        character_id: str = str(options["character_id"])
        if not character_id:
            self.stdout.write(self.style.ERROR("No character_id provided"))
            sys.exit(1)

        create: bool = options["create"]
        if create:
            character_instance, _ = CharacterModel.objects.get_or_create(
                mal_id=character_id
            )

        else:
            try:
                character_instance = CharacterModel.objects.get(mal_id=character_id)

            except CharacterModel.DoesNotExist:
                self.stdout.write(
                    f"No CharacterModel found for {self.style.ERROR(character_id)}"
                )
                sys.exit(1)

        res = self.client.get(f"https://myanimelist.net/character/{character_id}")

        parser = CharacterParser(res.text)
        data_dictionary = {k: v for k, v in parser.build_dictionary().items() if v}

        for attr, value in data_dictionary.items():
            # Special method
            if attr == "character_image":
                # value is of type ChacaterImage
                setattr(
                    character_instance,
                    attr,
                    ImageFile(
                        value["image"],
                        name=f"{character_id}.{value['mimetype'].lower()}",
                    ),
                )

            else:
                setattr(character_instance, attr, value)

        character_instance.save()
        self.stdout.write(f"Successfully got info for {self.style.SUCCESS(character_id)}")
