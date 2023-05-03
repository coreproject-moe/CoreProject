from apps.anime.models import AnimeModel
from apps.anime.models.anime_genre import AnimeGenreModel
from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ...schemas.anime.anime_genre import AnimeGenreGETSchema

router = Router()


@router.get("/{int:anime_id}/genres", response=list[AnimeGenreGETSchema])
def get_individual_anime_genre_info(
    request: HttpRequest,
    anime_id: int,
) -> list[AnimeGenreModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).genres,
    )
    return query
