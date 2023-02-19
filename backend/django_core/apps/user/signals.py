import inspect
from typing import TypedDict, Unpack

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import HttpRequest

from .models import CustomUser
from .utilities import get_client_ip, get_random_discriminator


class DjangoInstance(TypedDict):
    instance: CustomUser


@receiver(pre_save, sender=CustomUser)
def user_discriminator_handler(
    **kwargs: Unpack[DjangoInstance],
) -> None:
    instance = kwargs["instance"]
    if not instance.discriminator:
        instance.discriminator = get_random_discriminator(username=instance.username)


@receiver(pre_save, sender=CustomUser)
def user_ip_handler(
    **kwargs: Unpack[DjangoInstance],
) -> None:
    # https://stackoverflow.com/questions/4721771/get-current-user-log-in-signal-in-django
    request: HttpRequest | None = None
    # Reversed is better than not doing reverse
    # Source : Trust me bro
    for frame_record in reversed(inspect.stack()):
        if frame_record[3] == "get_response":
            request = frame_record[0].f_locals["request"]
            break

    instance: CustomUser = kwargs["instance"]

    # If we use `createsuperuser` we dont have any ip
    try:
        ip = get_client_ip(request)
    except AttributeError:
        ip = "0.0.0.0"

    instance.ip = ip
