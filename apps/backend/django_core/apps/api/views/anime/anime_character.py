from apps.anime.models import AnimeModel
from apps.api.auth import AuthBearer
from apps.api.decorator import permission_required
from apps.api.permissions import IsSuperUser
from apps.characters.models import CharacterModel
from apps.api.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router

from ...schemas.characters import CharacterGETSchema

router = Router()


@router.get("/{int:anime_id}/character", response=list[CharacterGETSchema])
def get_individual_anime_character_info(
    request: HttpRequest,
    anime_id: int,
) -> list[CharacterModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).characters,
    )
    return query


@router.post(
    "/{int:anime_id}/character",
    response=list[CharacterGETSchema],
    auth=AuthBearer(),
)
@permission_required([IsSuperUser])
def post_individual_anime_character_info(
    request: HttpRequest,
    anime_id: int,
    payload: CharacterGETSchema,
) -> CharacterModel:
    # Set this at top
    # Because if there is no anime_info_model with corresponding query
    # theres no point in continuing
    anime_info_model = get_object_or_404(AnimeModel, pk=anime_id)

    query = CharacterModel.objects.get_or_create(
        **payload.dict(),
    )
    instance: CharacterModel = query[0]
    anime_info_model.characters.add(instance)

    return instance
