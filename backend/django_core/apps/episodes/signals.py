from typing import TypedDict, Unpack


from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import EpisodeModel

from .tasks import upload_file_to_providers_and_set_thumbnail


class DjangoInstance(TypedDict):
    instance: EpisodeModel


@receiver(post_save, sender=EpisodeModel)
def banner_background_color_handler(
    **kwargs: Unpack[DjangoInstance],
) -> None:
    instance = kwargs["instance"]

    # Set Background Banner Image Color
    if hasattr(instance, "episode_file"):
        upload_file_to_providers_and_set_thumbnail.delay(pk=instance.pk)
