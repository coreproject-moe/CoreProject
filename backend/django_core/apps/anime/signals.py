from typing import Unpack, TypedDict
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import AnimeModel


class DjangoInstance(TypedDict):
    instance: AnimeModel


@receiver(pre_save, sender=AnimeModel)
def user_discriminator_handler(
    **kwargs: Unpack[DjangoInstance],
) -> None:
    instance = kwargs["instance"]
