from apps.anime.models import AnimeModel
from apps.producers.models import ProducerModel
from ninja import Router

from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404

from ...schemas.producers import ProducerSchema

router = Router()


@router.get("/{int:anime_id}/producers", response=list[ProducerSchema])
def get_individual_anime_producer_info(
    request: HttpRequest,
    anime_id: int,
) -> list[ProducerModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).producers,
    )
    return query


@router.post("/{int:anime_id}/producers", response=ProducerSchema)
def post_individual_anime_producer_info(
    request: HttpRequest,
    anime_id: int,
    payload: ProducerSchema,
) -> ProducerModel:
    # Set this at top
    # Because if there is no anime_info_model with corresponding query
    # theres no point in continuing
    anime_info_model = get_object_or_404(AnimeModel, pk=anime_id)

    query = ProducerModel.objects.get_or_create(
        **payload.dict(),
    )

    instance: ProducerModel = query[0]
    anime_info_model.producers.add(instance)

    return instance
