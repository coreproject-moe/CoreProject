from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import User
from .utilities import get_random_username_discriminator


@receiver(pre_save, sender=User)
def user_handler(sender, **kwargs):
    instance = kwargs["instance"]
    instance.username_discriminator = get_random_username_discriminator(
        username=instance.username
    )
