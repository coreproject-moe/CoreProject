from .models import AnimeModel
from core.utils.rgb_to_hex import rgb_to_hex
from colorthief import ColorThief
from celery import shared_task
from PIL import ImageStat, Image

import math


@shared_task()
def set_field_color(
    pk: int,
    field_name: str,
    image_field_name: str,
) -> None:
    instance = AnimeModel.objects.get(pk=pk)

    if image_field := getattr(instance, image_field_name):
        color = ColorThief(image_field.path).get_color(quality=1)
        rgb_value_to_hex = rgb_to_hex(color[0], color[1], color[2])
        setattr(
            instance,
            field_name,
            rgb_value_to_hex,
        )
        instance.save()
        print(f"Set color for | AnimeModel = {pk}")


@shared_task()
def set_field_brightness(
    pk: int,
    field_name: str,
    image_field_name: str,
):
    instance = AnimeModel.objects.get(pk=pk)

    if image_field := getattr(instance, image_field_name):
        # https://stackoverflow.com/a/3498247
        im = Image.open(image_field)
        stat = ImageStat.Stat(im)
        gs = (
            math.sqrt(0.241 * (r**2) + 0.691 * (g**2) + 0.068 * (b**2))
            for r, g, b in im.getdata()
        )
        average_brightness = sum(gs) / stat.count[0]
        setattr(instance, field_name, average_brightness)
        instance.save()
        print(f"Set brightness for | AnimeModel = {pk}")
