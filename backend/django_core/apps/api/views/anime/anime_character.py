
from apps.anime.models import AnimeModel
from apps.characters.models import CharacterModel
from ninja import Router

from django.http import HttpRequest
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
