from http import HTTPStatus

from apps.anime.models.anime_theme import AnimeThemeModel
from apps.api.auth import AuthBearer
from apps.user.models import CustomUser
from django.http import HttpRequest, HttpResponse
from ninja import Query, Router

from django_core.apps.api.decorator import permission_required
from django_core.apps.api.permissions import IsSuperUserOrReadOnly

from ...filters.themes import ThemeFilter
from ...schemas.anime.anime_theme import AnimeThemeGETSchema, AnimeThemePOSTSchema

router = Router()


@router.get("/themes", response=list[AnimeThemeGETSchema])
def get_anime_theme_info(
    request: HttpRequest,
    filters: ThemeFilter = Query(...),
) -> list[AnimeThemeModel]:
    query = AnimeThemeModel.objects.filter(
        type__icontains="anime",
        **filters.dict(exclude_none=True),
    )
    return query


@router.post("/themes", response=list[AnimeThemeGETSchema], auth=AuthBearer())
@permission_required([IsSuperUserOrReadOnly])
def post_anime_theme_info(
    request: HttpRequest,
    payload: list[AnimeThemePOSTSchema],
) -> list[AnimeThemeModel]:

    instance_objects = []
    for object in payload:
        instance_objects.append(
            AnimeThemeModel(
                type="anime",
                **object.dict(exclude_none=True),
            )
        )

    query = AnimeThemeModel.objects.bulk_create(instance_objects)
    return query
