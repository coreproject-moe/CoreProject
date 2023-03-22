from http import HTTPStatus

from apps.anime.models.anime_openings_and_endings import AnimeOpeningModel
from apps.api.auth import AuthBearer
from apps.user.models import CustomUser
from ninja import Router, Query

from django.http import HttpRequest, HttpResponse
from ...filters.openings import OpeningFilter
from ...schemas.anime.anime_opening import AnimeOpeningGETSchema, AnimeOpeningPOSTSchema

router = Router()


@router.get("/openings", response=list[AnimeOpeningGETSchema])
def get_anime_opening_info(
    request: HttpRequest,
    filters: OpeningFilter = Query(...),
) -> list[AnimeOpeningModel]:
    query = AnimeOpeningModel.objects.filter(**filters.dict(exclude_none=True))

    return query


@router.post("/openings", response=AnimeOpeningGETSchema, auth=AuthBearer())
def post_anime_opening_info(
    request: HttpRequest,
    payload: AnimeOpeningPOSTSchema,
) -> list[AnimeOpeningModel]:
    user: CustomUser = request.auth
    if not user.is_superuser:
        return HttpResponse(
            "Superuser is required for this operation", status=HTTPStatus.UNAUTHORIZED
        )

    instance_objects = []
    for object in payload:
        instance_objects.append(
            AnimeOpeningModel(
                **object.dict(exclude_none=True),
            )
        )

    query = AnimeOpeningModel.objects.create(instance_objects)
    return query
