from typing import List

from django.shortcuts import get_object_or_404, get_list_or_404
from ninja import Router

from ..models import AnimeInfoModel
from ..schemas import AnimeGenreSchema

router = Router()


@router.get("/info/{int:anime_id}/genres", response=List[AnimeGenreSchema])
def get_individual_anime_genre_info(request, anime_id: int):
    query = get_list_or_404(get_object_or_404(AnimeInfoModel, id=anime_id).anime_genres)
    return query
