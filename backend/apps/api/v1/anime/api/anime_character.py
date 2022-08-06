from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router
from django.http import HttpRequest

from ..models import AnimeInfoModel
from ..schemas import AnimeCharacterSchema

router = Router()


@router.get("/info/{int:anime_id}/character", response=list[AnimeCharacterSchema])
def get_individual_anime_character_info(request: HttpRequest, anime_id: int):
    query = get_list_or_404(
        get_object_or_404(AnimeInfoModel, id=anime_id).anime_characters
    )

    return query
