from http import HTTPStatus

from apps.anime.models import AnimeModel
from apps.api.auth import AuthBearer
from apps.characters.models import CharacterModel
from apps.user.models import CustomUser
from ninja import Router

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404

from ...schemas.characters import CharacterSchema

router = Router()


@router.get("/{int:anime_id}/character", response=list[CharacterSchema])
def get_individual_anime_character_info(
    request: HttpRequest,
    anime_id: int,
) -> list[CharacterModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).characters,
    )
    return query
