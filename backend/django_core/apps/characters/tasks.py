from celery import shared_task
from django.core.management import call_command
from django.db.models import Q
from django.utils import timezone

from shinobi.builder.character import CharacterBuilder

from .models import CharacterModel

# Beat tasks


@shared_task()
def get_periodic_character() -> None:
    builder = CharacterBuilder()

    # TODO Order the first query higher
    instances = CharacterModel.objects.filter(
        (
            (
                Q(name__isnull=True)
                | Q(name_kanji__isnull=True)
                | Q(character_image__isnull=True)
                | Q(about__isnull=True)
            )
            | (Q(updated_at__gte=timezone.now() - timezone.timedelta(days=14)))
        )
        & Q(is_locked=False)
    )

    dictionary = builder.build_dictionary(
        excluded_ids=list(instances.values_list("pk", flat=True)),
        sort=True,
    )

    for character in list(dictionary.keys()):
        call_character_command.delay(character)


# Call Commands


@shared_task()
def call_character_command(id: int) -> None:
    call_command("get_character", id, create=True)
