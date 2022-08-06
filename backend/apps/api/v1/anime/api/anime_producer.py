from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ..models import AnimeInfoModel, AnimeProducerModel
from ..schemas import AnimeProducerSchema

router = Router()


@router.get("/info/{int:anime_id}/producers", response=list[AnimeProducerSchema])
def get_individual_anime_producer_info(request: HttpRequest, anime_id: int):
    query = get_list_or_404(
        get_object_or_404(AnimeInfoModel, id=anime_id).anime_producers
    )
    return query


@router.post("/info/{int:anime_id}/producers", response=AnimeProducerSchema)
def post_individual_anime_producer_info(
    request: HttpRequest, anime_id: int, payload: AnimeProducerSchema
):
    instance, created = AnimeProducerModel.objects.get_or_create(
        **payload.dict(),
    )
    AnimeInfoModel.objects.get(pk=anime_id).anime_producers.add(instance)

    return instance
