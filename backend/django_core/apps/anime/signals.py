from typing import Unpack, TypedDict
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from .models import AnimeModel

import numpy
from apps.anime.tasks import set_field_brightness


class DjangoInstance(TypedDict):
    instance: AnimeModel


@receiver(post_save, sender=AnimeModel)
def banner_background_color_handler(
    **kwargs: Unpack[DjangoInstance],
) -> None:
    instance = kwargs["instance"]

    # Set Background Banner Image Color
    if (
        instance_banner_background_image := getattr(instance, "banner", None)
    ) and not instance.banner_background_color:
        set_field_brightness(
            instance.pk,
            "banner_background_color",
            instance_banner_background_image,
        )

    # Set Background Cover Image Color
    if (
        instance_cover_background_image := getattr(instance, "cover", None)
    ) and not instance.cover_background_color:
        set_field_brightness(
            instance.pk,
            "cover_background_color",
            instance_cover_background_image,
        )
