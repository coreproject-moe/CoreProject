from apps.anime.models import AnimeModel
from apps.producers.models import ProducerModel
from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ...schemas.producers import ProducerGETSchema

router = Router()


@router.get("/{int:anime_id}/producers", response=list[ProducerGETSchema])
def get_individual_anime_producer_info(
    request: HttpRequest,
    anime_id: int,
) -> list[ProducerModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).producers,
    )
    return query
