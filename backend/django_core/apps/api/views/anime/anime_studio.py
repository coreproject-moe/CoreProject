from http import HTTPStatus
from apps.anime.models import AnimeModel
from apps.studios.models import StudioModel
from ninja import Router
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404

from apps.api.auth import AuthBearer
from apps.user.models import CustomUser
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


@router.post("/{int:anime_id}/studios", response=StudioSchema, auth=AuthBearer())
def post_individual_anime_studio_info(
    request: HttpRequest,
    anime_id: int,
    payload: StudioSchema,
) -> StudioModel:
    user: CustomUser = request.auth
    if not user.is_superuser:
        raise HttpResponse(
            "Superuser is required for this operation", status=HTTPStatus.UNAUTHORIZED
        )
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
