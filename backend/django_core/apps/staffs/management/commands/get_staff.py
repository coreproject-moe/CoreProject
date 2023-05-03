import sys
from typing import NoReturn

from django.core.management.base import BaseCommand

from shinobi.parser.staff import StaffParser
from shinobi.utilities.session import session

from ...models import StaffAlternateNameModel, StaffModel


class Command(BaseCommand):
    help = "Django command that gets the Staff Information given mal_id"

    def __init__(self, *args, **kwargs) -> None:
        self.client = session
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument(
            "staff_id",
            type=int,
            help="The staff number to get information for",
        )

    def handle(self, *args, **options) -> NoReturn:
        staff_id: int = options["staff_id"]
        res = self.client.get(f"https://myanimelist.net/people/{staff_id}")

        parser = StaffParser(res.text)
        data_dictionary = parser.build_dictionary()

        try:
            staff_instance = StaffModel.objects.get(mal_id=staff_id)
        except StaffModel.DoesNotExist:
            self.stdout.write(f"No StaffModel found for {self.style.ERROR(staff_id)}")
            sys.exit(1)

        if alternate_name := data_dictionary.pop("alternate_name"):
            for name in alternate_name:
                instance, created = StaffAlternateNameModel.objects.get_or_create(name)
                if created:
                    StaffModel.alternate_names.add(instance)

        for attr, value in data_dictionary.items():
            if value:
                setattr(staff_instance, attr, value)

        staff_instance.save()

        self.stdout.write(f"Successfully got info for {self.style.SUCCESS(staff_id)}")
