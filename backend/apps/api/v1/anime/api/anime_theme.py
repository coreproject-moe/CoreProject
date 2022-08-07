from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ..models import AnimeModel, AnimeThemeModel
from ..schemas import AnimeThemeSchema

router = Router()


@router.get("/{int:anime_id}/themes", response=list[AnimeThemeSchema])
def get_individual_anime_theme_info(request: HttpRequest, anime_id: int):
    query = get_list_or_404(
        get_object_or_404(AnimeModel, id=anime_id).anime_themes,
    )
    return query


@router.post("/{int:anime_id}/themes", response=AnimeThemeSchema)
def post_individual_anime_theme_info(
    request: HttpRequest, anime_id: int, payload: AnimeThemeSchema
):
    # Set this at top
    # Because if there is no anime_info_model with corresponding query theres no point in  continuing
    anime_info_model = get_object_or_404(AnimeModel, pk=anime_id)

    instance, created = AnimeThemeModel.objects.get_or_create(
        **payload.dict(),
    )
    anime_info_model.anime_studios.add(instance)

    return instance
