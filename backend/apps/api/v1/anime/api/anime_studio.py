from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ..models import AnimeInfoModel, AnimeStudioModel
from ..schemas import AnimeStudioSchema

router = Router()


@router.get("/info/{int:anime_id}/studios", response=list[AnimeStudioSchema])
def get_individual_anime_studio_info(request: HttpRequest, anime_id: int):
    query = get_list_or_404(
        get_object_or_404(AnimeInfoModel, id=anime_id).anime_studios
    )

    return query


@router.post("/info/{int:anime_id}/studios", response=AnimeStudioSchema)
def post_individual_anime_studio_info(
    request: HttpRequest, anime_id: int, payload: AnimeStudioSchema
):
    instance, created = AnimeStudioModel.objects.get_or_create(
        **payload.dict(),
    )
    AnimeInfoModel.objects.get(pk=anime_id).anime_studios.add(instance)

    return instance
