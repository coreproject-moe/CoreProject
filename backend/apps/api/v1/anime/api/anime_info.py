from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from ..models import AnimeInfoModel
from ..schemas import AnimeInfoSchema

router = Router()


@router.get("/info", response=list[AnimeInfoSchema])
def get_anime_info(request):
    return AnimeInfoModel.objects.all()


@router.get("/info/{anime_id}", response=AnimeInfoSchema)
def get_individual_anime_info(request, anime_id: int):
    query = get_object_or_404(AnimeInfoModel, id=anime_id)
    return query
