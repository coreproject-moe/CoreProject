import sys
from argparse import ArgumentParser, Namespace

from django.core.management.base import BaseCommand

from shinobi.parser.producer import ProducerParser
from shinobi.utilities.session import session

from ...models import ProducerModel
from typing import Any


def get_periodic_producers():
    pass


class Command(BaseCommand):
    help = "Django command that gets the Producer Information given mal_id"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.client = session
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "producer_id",
            type=int,
            help="The producer number to get information for",
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

    def handle(self, *args: Any, **options: dict[str, Any]) -> None:
        periodic: bool = bool(options["periodic"])
        if periodic:
            get_periodic_producers.delay()
            self.stdout.write("Successfully stated preiodic celery commands")
            sys.exit(0)

        producer_id = str(options["producer_id"])
        if not producer_id:
            self.stdout.write(self.style.ERROR("No producer_id provided"))
            sys.exit(1)

        create: bool = bool(options["create"])
        if create:
            producer_instance, _ = ProducerModel.objects.get_or_create(mal_id=producer_id)
        else:
            try:
                producer_instance = ProducerModel.objects.get(mal_id=producer_id)
            except ProducerModel.DoesNotExist:
                self.stdout.write(
                    f"No ProducerModel found for {self.style.ERROR(producer_id)}"
                )
                sys.exit(1)

        res = self.client.get(f"https://myanimelist.net/anime/producer/{producer_id}")

        parser = ProducerParser(res.text)
        data_dictionary = {k: v for k, v in parser.build_dictionary().items() if v}

        for attr, value in data_dictionary.items():
            if value:
                setattr(producer_instance, attr, value)

        producer_instance.save()
        self.stdout.write(f"Successfully got info for {self.style.SUCCESS(producer_id)}")
