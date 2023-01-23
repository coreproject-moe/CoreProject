from huey.contrib.djhuey import db_task
from .models import AnimeModel
from core.utils.rgb_to_hex import rgb_to_hex
from core.utils.k_means_color_analyzer import KMeansColorAnalyzer
from numpy.typing import NDArray
import logging

logger = logging.getLogger(__name__)


@db_task()
def set_field_brightness(
    pk: int,
    field_name: str,
    image: NDArray,
) -> None:
    rgb_tuple = KMeansColorAnalyzer(image).best_color()
    instance = AnimeModel.objects.get(pk=pk)
    setattr(
        instance,
        field_name,
        rgb_to_hex(
            red=int(rgb_tuple[0]),
            green=int(rgb_tuple[1]),
            blue=int(rgb_tuple[2]),
        ),
    )
    instance.save()
    logger.info(f"Set color for | AnimeModel = {pk}")
