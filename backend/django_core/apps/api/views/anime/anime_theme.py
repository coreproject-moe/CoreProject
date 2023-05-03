from apps.anime.models import AnimeModel
from apps.anime.models.anime_theme import AnimeThemeModel
from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ...schemas.anime.anime_theme import AnimeThemeGETSchema

router = Router()


@router.get("/{int:anime_id}/themes", response=list[AnimeThemeGETSchema])
def get_individual_anime_theme_info(
    request: HttpRequest,
    anime_id: int,
) -> list[AnimeThemeModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).themes,
    )
    return query
