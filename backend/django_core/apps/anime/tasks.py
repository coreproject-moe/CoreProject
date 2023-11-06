import math

from celery import shared_task
from modern_colorthief import ColorThief
from django.core.management import call_command
from django.db.models import Q
from django.utils import timezone
from PIL import Image, ImageStat
from utilities.rgb_to_hex import rgb_to_hex

from shinobi.builder.anime import AnimeBuilder
from shinobi.builder.genre import AnimeGenreBuilder
from shinobi.builder.theme import AnimeThemeBuilder

from .models import AnimeModel

# Beat tasks


@shared_task()
def get_periodic_anime_genres() -> None:
    builder = AnimeGenreBuilder()
    dictionary = builder.build_dictionary()

    for genre in list(dictionary.keys()):
        call_anime_genre_command.delay(genre)


@shared_task()
def get_periodic_anime_themes() -> None:
    builder = AnimeThemeBuilder()
    dictionary = builder.build_dictionary()

    for theme in list(dictionary.keys()):
        call_anime_theme_command.delay(theme)


@shared_task()
def get_periodic_anime() -> None:
    builder = AnimeBuilder()
    instances = AnimeModel.objects.filter(
        Q(updated_at__gte=timezone.now() - timezone.timedelta(days=7)) & Q(is_locked=False)
    )

    dictionary = builder.build_dictionary(
        excluded_ids=list(instances.values_list("pk", flat=True))
    )

    for anime in list(dictionary.keys()):
        call_anime_command.delay(anime)


# Calls
@shared_task()
def call_anime_genre_command(id: int) -> None:
    call_command("get_anime_genre", id)


@shared_task()
def call_anime_theme_command(id: int) -> None:
    call_command("get_anime_theme", id)


@shared_task()
def call_anime_command(id: int) -> None:
    call_command("get_anime", id, create=True)


# Setters


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
