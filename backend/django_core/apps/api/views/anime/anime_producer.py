from http import HTTPStatus

from apps.anime.models import AnimeModel
from apps.api.auth import AuthBearer
from apps.producers.models import ProducerModel
from apps.user.models import CustomUser
from ninja import Router

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404

from ...schemas.producers import ProducerGETSchema

router = Router()


@router.get("/{int:anime_id}/producers", response=list[ProducerGETSchema])
def get_individual_anime_producer_info(
    request: HttpRequest,
    anime_id: int,
) -> list[ProducerModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).producers,
    )
    return query


@router.post("/{int:anime_id}/producers", response=ProducerGETSchema, auth=AuthBearer())
def post_individual_anime_producer_info(
    request: HttpRequest,
    anime_id: int,
    payload: ProducerGETSchema,
) -> ProducerModel:
    user: CustomUser = request.auth
    if not user.is_superuser:
        raise HttpResponse(
            "Superuser is required for this operation",
            status=HTTPStatus.UNAUTHORIZED,
        )
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
