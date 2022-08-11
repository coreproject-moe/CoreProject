from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import User
from .utilities import get_random_username_discriminator


@receiver(pre_save, sender=User)
def user_discriminator_handler(**kwargs):
    instance = kwargs["instance"]
    if not instance.username_discriminator:
        instance.username_discriminator = get_random_username_discriminator(
            username=instance.username
        )
