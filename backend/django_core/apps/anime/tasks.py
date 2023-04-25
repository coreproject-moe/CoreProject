import math

from PIL import Image, ImageStat
from celery import shared_task
from colorthief import ColorThief
from utilities.rgb_to_hex import rgb_to_hex

from django.core.management import call_command

from .models import AnimeModel

from shinobi.builder.genre import AnimeGenreBuilder
from shinobi.builder.theme import AnimeThemeBuilder


@shared_task
def get_preiodic_anime_genres():
    builder = AnimeGenreBuilder()
    dictionary = builder.build_dictionary()

    for genre in list(dictionary.keys()):
        call_command("get_anime_genre", genre_id=genre)


@shared_task
def get_preiodic_anime_themes():
    builder = AnimeThemeBuilder()
    dictionary = builder.build_dictionary()

    for theme in list(dictionary.keys()):
        call_command("get_anime_theme", theme_id=theme)


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
) -> None:
    instance = AnimeModel.objects.get(pk=pk)

    if image_field := getattr(instance, image_field_name):
        # https://stackoverflow.com/a/3498247
        im = Image.open(image_field)
        stat = ImageStat.Stat(im)
        gs = (
            math.sqrt(0.241 * (red**2) + 0.691 * (green**2) + 0.068 * (blue**2))
            for red, green, blue in im.getdata()
        )
        average_brightness = sum(gs) / stat.count[0]
        setattr(instance, field_name, average_brightness)
        instance.save()
        print(f"Set brightness for | AnimeModel = {pk}")
