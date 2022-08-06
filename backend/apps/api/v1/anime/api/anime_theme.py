from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ..models import AnimeInfoModel, AnimeThemeModel
from ..schemas import AnimeThemeSchema

router = Router()


@router.get("/info/{int:anime_id}/themes", response=list[AnimeThemeSchema])
def get_individual_anime_theme_info(request: HttpRequest, anime_id: int):
    query = get_list_or_404(get_object_or_404(AnimeInfoModel, id=anime_id).anime_themes)
    return query


@router.post("/info/{int:anime_id}/themes", response=AnimeThemeSchema)
def post_individual_anime_theme_info(
    request: HttpRequest, anime_id: int, payload: AnimeThemeSchema
):
    instance, created = AnimeThemeModel.objects.get_or_create(
        **payload.dict(),
    )
    AnimeInfoModel.objects.get(pk=anime_id).anime_studios.add(instance)

    return instance
