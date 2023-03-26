from typing import TypedDict, Unpack

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import CustomUser
from .utilities import get_random_discriminator


class DjangoInstance(TypedDict):
    instance: CustomUser


@receiver(pre_save, sender=CustomUser)
def user_discriminator_handler(
    **kwargs: Unpack[DjangoInstance],
) -> None:
    instance = kwargs["instance"]
    if not instance.discriminator:
        instance.discriminator = get_random_discriminator(username=instance.username)
