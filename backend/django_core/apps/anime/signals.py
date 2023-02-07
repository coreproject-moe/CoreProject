from typing import TypedDict, Unpack

from apps.anime.tasks import set_field_color

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import AnimeModel


class DjangoInstance(TypedDict):
    instance: AnimeModel


@receiver(post_save, sender=AnimeModel)
def banner_background_color_handler(
    **kwargs: Unpack[DjangoInstance],
) -> None:
    instance = kwargs["instance"]

    # Set Background Banner Image Color
    if (hasattr(instance, "banner")) and not instance.banner_background_color:
        set_field_color.delay(
            instance.pk,
            "banner_background_color",
            "banner",
        )

    # Set Background Cover Image Color
    if (hasattr(instance, "cover")) and not instance.cover_background_color:
        set_field_color.delay(
            instance.pk,
            "cover_background_color",
            "cover",
        )
