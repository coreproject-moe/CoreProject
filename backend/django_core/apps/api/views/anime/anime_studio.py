from http import HTTPStatus

from apps.anime.models import AnimeModel
from apps.api.auth import AuthBearer
from apps.user.models import CustomUser
from ninja import Router

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404

from ....producers.models import ProducerModel
from ...schemas.producers import ProducerGETSchema, ProducerPOSTSchema

router = Router()


@router.get("/{int:anime_id}/studios", response=list[ProducerGETSchema])
def get_individual_anime_studio_info(
    request: HttpRequest,
    anime_id: int,
) -> list[ProducerModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).studios,
    )

    return query
