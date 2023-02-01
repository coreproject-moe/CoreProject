from apps.anime.models import AnimeModel
from apps.studios.models import StudioModel
from ninja import Router

from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404

from ...schemas.studios import StudioSchema

router = Router()


@router.get("/{int:anime_id}/studios", response=list[StudioSchema])
def get_individual_anime_studio_info(
    request: HttpRequest,
    anime_id: int,
) -> list[StudioModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).studios,
    )

    return query


@router.post("/{int:anime_id}/studios", response=StudioSchema)
def post_individual_anime_studio_info(
    request: HttpRequest,
    anime_id: int,
    payload: StudioSchema,
) -> StudioModel:
    # Set this at top
    # Because if there is no anime_info_model with corresponding query
    # theres no point in continuing
    anime_info_model = get_object_or_404(AnimeModel, pk=anime_id)

    query = StudioModel.objects.get_or_create(
        **payload.dict(),
    )

    instance: StudioModel = query[0]
    anime_info_model.studios.add(instance)

    return instance
