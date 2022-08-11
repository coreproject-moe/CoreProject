from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ...characters.models import CharacterModel
from ...characters.schemas import CharacterSchema
from ..models import AnimeModel

router = Router()


@router.get("/{int:anime_id}/character", response=list[CharacterSchema])
def get_individual_anime_character_info(request: HttpRequest, anime_id: int):
    query = get_list_or_404(
        get_object_or_404(AnimeModel, id=anime_id).anime_characters,
    )
    return query


@router.post("/{int:anime_id}/character", response=list[CharacterSchema])
def post_individual_anime_character_info(
    request: HttpRequest, anime_id: int, payload: CharacterSchema
):
    # Set this at top
    # Because if there is no anime_info_model with corresponding query theres no point in  continuing
    anime_info_model = get_object_or_404(AnimeModel, pk=anime_id)

    instance, created = CharacterModel.objects.get_or_create(
        **payload.dict(),
    )
    anime_info_model.anime_characters.add(instance)

    return instance
