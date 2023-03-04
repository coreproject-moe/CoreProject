from http import HTTPStatus

from apps.anime.models import AnimeModel
from apps.anime.models.anime_theme import AnimeThemeModel
from apps.api.auth import AuthBearer
from apps.user.models import CustomUser
from ninja import Router

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404

from ...schemas.anime.anime_theme import AnimeThemeGETSchema

router = Router()


@router.get("/{int:anime_id}/themes", response=list[AnimeThemeGETSchema])
def get_individual_anime_theme_info(
    request: HttpRequest,
    anime_id: int,
) -> list[AnimeThemeModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).themes,
    )
    return query


@router.post("/{int:anime_id}/themes", response=AnimeThemeGETSchema, auth=AuthBearer())
def post_individual_anime_theme_info(
    request: HttpRequest,
    anime_id: int,
    payload: AnimeThemeGETSchema,
) -> AnimeThemeModel:
    user: CustomUser = request.auth
    if not user.is_superuser:
        raise HttpResponse(
            "Superuser is required for this operation", status=HTTPStatus.UNAUTHORIZED
        )

    anime_info_model = get_object_or_404(AnimeModel, pk=anime_id)
    instance_objects = []
    for object in payload:
        instance_objects.append(
            AnimeThemeModel(
                type="anime",
                **object.dict(exclude_none=True),
            )
        )

    instance = AnimeThemeModel.objects.bulk_create(instance_objects)
    anime_info_model.themes.add(instance)

    return instance
