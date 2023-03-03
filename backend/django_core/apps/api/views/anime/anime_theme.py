from http import HTTPStatus
from apps.anime.models import AnimeModel
from apps.anime.models.anime_theme import AnimeThemeModel
from ninja import Router

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404

from apps.api.auth import AuthBearer
from apps.user.models import CustomUser
from ...schemas.anime.anime_theme import AnimeThemeSchema

router = Router()


@router.get("/{int:anime_id}/themes", response=list[AnimeThemeSchema])
def get_individual_anime_theme_info(
    request: HttpRequest,
    anime_id: int,
) -> list[AnimeThemeModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).themes,
    )
    return query


@router.post("/{int:anime_id}/themes", response=AnimeThemeSchema, auth=AuthBearer())
def post_individual_anime_theme_info(
    request: HttpRequest,
    anime_id: int,
    payload: AnimeThemeSchema,
) -> AnimeThemeModel:
    user: CustomUser = request.auth
    if not user.is_superuser:
        raise HttpResponse(
            "Superuser is required for this operation", status=HTTPStatus.UNAUTHORIZED
        )
    # Set this at top
    # Because if there is no anime_info_model with corresponding query
    # theres no point in  continuing
    anime_info_model = get_object_or_404(AnimeModel, pk=anime_id)

    query = AnimeThemeModel.objects.get_or_create(
        **payload.dict(),
    )

    instance: AnimeThemeModel = query[0]
    anime_info_model.themes.add(instance)

    return instance
