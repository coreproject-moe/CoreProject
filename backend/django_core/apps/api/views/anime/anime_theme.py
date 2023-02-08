from apps.anime.models import AnimeModel
from apps.anime.models.anime_theme import AnimeThemeModel
from ninja import Router

from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404

from ...schemas.anime.anime_theme import AnimeThemeSchema

router = Router()


@router.get("/{int:anime_id}/themes", response=list[AnimeThemeSchema])
def get_individual_anime_theme_info(
    request: HttpRequest,
    anime_id: int,
) -> list[AnimeThemeModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).themes,
    )
    return query


@router.post("/{int:anime_id}/themes", response=AnimeThemeSchema)
def post_individual_anime_theme_info(
    request: HttpRequest,
    anime_id: int,
    payload: AnimeThemeSchema,
) -> AnimeThemeModel:
    # Set this at top
    # Because if there is no anime_info_model with corresponding query
    # theres no point in  continuing
    anime_info_model = get_object_or_404(AnimeModel, pk=anime_id)

    query = AnimeThemeModel.objects.get_or_create(
        **payload.dict(),
    )

    instance: AnimeThemeModel = query[0]
    anime_info_model.studios.add(instance)

    return instance
