from http import HTTPStatus

from apps.anime.models.anime_openings_and_endings import AnimeEndingModel
from apps.api.auth import AuthBearer
from apps.user.models import CustomUser
from django.http import HttpRequest, HttpResponse
from ninja import File, Form, Query, Router
from ninja.files import UploadedFile
from pydantic import AnyUrl

from django_core.apps.api.decorator import permission_required
from django_core.apps.api.permissions import IsSuperUserOrReadOnly

from ...filters.openings_and_endings import OpeningAndEndingFilter
from ...schemas.anime.anime_opening_and_ending import AnimeOpeningAndEndingGETSchema

router = Router()


@router.get("/endings", response=list[AnimeOpeningAndEndingGETSchema])
def get_anime_ending_info(
    request: HttpRequest,
    filters: OpeningAndEndingFilter = Query(...),
) -> list[AnimeEndingModel]:
    query = AnimeEndingModel.objects.filter(**filters.dict(exclude_none=True))

    return query


@router.post("/endings", response=AnimeOpeningAndEndingGETSchema, auth=AuthBearer())
@permission_required([IsSuperUserOrReadOnly])
def post_anime_ending_info(
    request: HttpRequest,
    entry: int | None = Form(...),
    name: str | None = Form(...),
    url: AnyUrl = Form(...),
    thumbnail: UploadedFile | None = File(...),
) -> AnimeEndingModel:
    query = AnimeEndingModel.objects.create(
        entry=entry,
        name=name,
        url=url,
        thumbnail=thumbnail,
    )
    return query
