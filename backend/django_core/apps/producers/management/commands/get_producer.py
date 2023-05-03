import sys
from typing import NoReturn

from django.core.management.base import BaseCommand

from shinobi.parser.producer import ProducerParser
from shinobi.utilities.session import session

from ...models import ProducerModel


class Command(BaseCommand):
    help = "Django command that gets the Producer Information given mal_id"

    def __init__(self, *args, **kwargs) -> None:
        self.client = session
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument(
            "producer_number",
            type=int,
            help="The producer number to get information for",
        )

    def handle(self, *args, **options) -> NoReturn:
        producer_number: int = options["producer_number"]
        res = self.client.get(f"https://myanimelist.net/anime/producer/{producer_number}")

        parser = ProducerParser(res.text)
        data_dictionary = parser.build_dictionary()

        try:
            producer_instance = ProducerModel.objects.get(mal_id=producer_number)
        except ProducerModel.DoesNotExist:
            self.stdout.write(
                f"No ProducerModel found for {self.style.ERROR(producer_number)}"
            )
            sys.exit(1)

        for attr, value in data_dictionary.items():
            if value:
                setattr(producer_instance, attr, value)

        producer_instance.save()
        self.stdout.write(
            f"Successfully got info for {self.style.SUCCESS(producer_number)}"
        )
