from typing import TypedDict, Unpack

from .tasks import set_field_color, set_field_brightness

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ImageWithBrightnessAndBackgroundColor


class DjangoInstance(TypedDict):
    instance: ImageWithBrightnessAndBackgroundColor


@receiver(post_save, sender=ImageWithBrightnessAndBackgroundColor)
def background_color_handler(
    **kwargs: Unpack[DjangoInstance],
) -> None:
    instance = kwargs["instance"]

    # Set Background Banner Image Color
    set_field_color.delay(
        pk=instance.pk,
        field_name="background_color",  # The field that contains the background color
        image_field_name="image",  # The field that contains the image
    )


@receiver(post_save, sender=ImageWithBrightnessAndBackgroundColor)
def brightness_handler(
    **kwargs: Unpack[DjangoInstance],
) -> None:
    instance = kwargs["instance"]

    # Set Background Banner Image Color
    set_field_brightness.delay(
        pk=instance.pk,
        field_name="brightness",
        image_field_name="image",
    )
