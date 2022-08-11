import inspect

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import User
from .utilities import get_client_ip, get_random_username_discriminator


@receiver(pre_save, sender=User)
def user_discriminator_handler(**kwargs):
    instance: User = kwargs["instance"]
    if not instance.username_discriminator:
        instance.username_discriminator = get_random_username_discriminator(
            username=instance.username
        )


@receiver(pre_save, sender=User)
def user_ip_handler(**kwargs):
    # https://stackoverflow.com/questions/4721771/get-current-user-log-in-signal-in-django
    request = None
    print(inspect.stack())
    for frame_record in inspect.stack():
        if frame_record[3] == "get_response":
            request = frame_record[0].f_locals["request"]
            break

    instance: User = kwargs["instance"]

    instance.ip = get_client_ip(request)
