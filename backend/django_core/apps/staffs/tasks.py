from celery import shared_task
from django.core.management import call_command
from django.db.models import Q
from django.utils import timezone

from shinobi.builder.staff import StaffBuilder

from .models import StaffModel


@shared_task()
def get_periodic_staff():
    builder = StaffBuilder()

    instances = StaffModel.objects.filter(
        (
            (
                Q(name__isnull=True)
                | Q(given_name__isnull=True)
                | Q(family_name__isnull=True)
                | Q(alternate_names__isnull=True)
                | Q(staff_image__isnull=True)
                | Q(about__isnull=True)
            )
            | Q(updated_at__gte=timezone.now() - timezone.timedelta(days=7))
        )
        & Q(is_locked=False)
    )
    dictionary = builder.build_dictionary(
        excluded_ids=instances.values_list("pk", flat=True),
        sort=True,
    )

    for staff in list(dictionary.keys()):
        call_staff_command.delay(staff)


# Call commands


def call_staff_command(id: int):
    call_command("get_staff", staff_id=id)
