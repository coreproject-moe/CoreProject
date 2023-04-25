from celery import shared_task

from shinobi.builder.character import CharacterBuilder

from django.core.management import call_command
from django.db.models import Q
from django.utils import timezone

from .models import CharacterModel


@shared_task()
def get_perodic_character():
    builder = CharacterBuilder()

    instances = CharacterModel.objects.filter(
        Q(updated_at__gte=timezone.now() - timezone.timedelta(days=7)) & Q(is_locked=False)
    )
    dictionary = builder.build_dictionary(
        excluded_ids=instances.values_list("pk", flat=True)
    )

    for character in list(dictionary.keys()):
        call_command("get_character", character_id=character)
