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
    if instance_banner_backgroud_image := getattr(instance, "banner", None):
        banner_background_image = Image.open(instance_banner_backgroud_image)
        banner_background_image_numpy_array = numpy.array(banner_background_image)
        set_field_brightness(
            instance.pk,
            "banner_background_color",
            banner_background_image_numpy_array,
        )()

    # Set Background Cover Image Color
    if instance_cover_background_image := getattr(instance, "cover", None):
        cover_background_image = Image.open(instance_cover_background_image)
        cover_background_image_numpy_array = numpy.array(cover_background_image)
        set_field_brightness(
            instance.pk,
            "cover_background_color",
            cover_background_image_numpy_array,
        )()
