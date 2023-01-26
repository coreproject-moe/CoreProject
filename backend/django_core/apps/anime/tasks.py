from .models import AnimeModel
from core.utils.rgb_to_hex import rgb_to_hex
from colorthief import ColorThief
from celery import shared_task


@shared_task()
def set_field_color(
    pk: int,
    field_name: str,
    image_field_name: str,
) -> None:
    instance = AnimeModel.objects.get(pk=pk)

    if image_field := getattr(instance, image_field_name):
        color = ColorThief(image_field.path).get_color(quality=1)
        setattr(
            instance,
            field_name,
            rgb_to_hex(
                color[0],
                color[1],
                color[2],
            ),
        )
        instance.save()
        print(f"Set color for | AnimeModel = {pk}")
