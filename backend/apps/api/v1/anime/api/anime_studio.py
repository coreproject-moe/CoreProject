from typing import List

from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ..models import AnimeInfoModel
from ..schemas import AnimeStudioSchema

router = Router()


@router.get("/info/{int:anime_id}/studios", response=list[AnimeStudioSchema])
def get_individual_anime_studio_info(request, anime_id: int):
    query = get_list_or_404(
        get_object_or_404(AnimeInfoModel, id=anime_id).anime_studios
    )

    return query
