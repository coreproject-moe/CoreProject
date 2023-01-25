from huey.contrib.djhuey import db_task
from .models import AnimeModel
from core.utils.rgb_to_hex import rgb_to_hex
from typing import BinaryIO

from colorthief import ColorThief


@db_task()
def set_field_color(
    pk: int,
    field_name: str,
    file: BinaryIO,
) -> None:
    instance = AnimeModel.objects.get(pk=pk)
    color = ColorThief(file).get_color(quality=1)
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
