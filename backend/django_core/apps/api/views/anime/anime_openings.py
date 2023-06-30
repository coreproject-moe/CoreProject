from apps.anime.models import AnimeModel
from apps.anime.models.anime_openings_and_endings import AnimeOpeningModel
from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ...schemas.anime.anime_opening_and_ending import AnimeOpeningAndEndingGETSchema

router = Router()


@router.get("/{int:anime_id}/openings", response=list[AnimeOpeningAndEndingGETSchema])
def get_individual_anime_opening_info(
    request: HttpRequest,
    anime_id: int,
) -> list[AnimeOpeningModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).openings,
    )
    return query
