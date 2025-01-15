from apps.anime.models import AnimeModel
from apps.producers.models import ProducerModel
from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ...schemas.staffs import StaffGETSchema

router = Router()


@router.get("/{int:anime_id}/staffs", response=list[StaffGETSchema])
def get_individual_anime_staff_info(
    request: HttpRequest,
    anime_id: int,
) -> list[ProducerModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).staffs,
    )
    return query
