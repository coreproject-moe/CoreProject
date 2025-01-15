from apps.anime.models import AnimeModel
from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ....producers.models import ProducerModel
from ...schemas.producers import ProducerGETSchema

router = Router()


@router.get("/{int:anime_id}/studios", response=list[ProducerGETSchema])
def get_individual_anime_studio_info(
    request: HttpRequest,
    anime_id: int,
) -> list[ProducerModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).studios,
    )

    return query
