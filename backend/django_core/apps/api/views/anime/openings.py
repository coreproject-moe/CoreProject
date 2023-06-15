
from apps.anime.models.anime_openings_and_endings import AnimeOpeningModel
from apps.api.auth import AuthBearer
from apps.api.decorator import permission_required
from apps.api.permissions import IsSuperUser
from django.http import HttpRequest
from ninja import File, Form, Query, Router
from ninja.files import UploadedFile
from pydantic import AnyUrl

from ...filters.openings_and_endings import OpeningAndEndingFilter
from ...schemas.anime.anime_opening_and_ending import AnimeOpeningAndEndingGETSchema

router = Router()


@router.get("/openings", response=list[AnimeOpeningAndEndingGETSchema])
def get_anime_opening_info(
    request: HttpRequest,
    filters: OpeningAndEndingFilter = Query(...),
) -> list[AnimeOpeningModel]:
    query = AnimeOpeningModel.objects.filter(**filters.dict(exclude_none=True))

    return query


@router.post("/openings", response=AnimeOpeningAndEndingGETSchema, auth=AuthBearer())
@permission_required([IsSuperUser])
def post_anime_opening_info(
    request: HttpRequest,
    entry: int | None = Form(...),
    name: str | None = Form(...),
    url: AnyUrl = Form(...),
    thumbnail: UploadedFile | None = File(...),
) -> AnimeOpeningModel:
    query = AnimeOpeningModel.objects.create(
        entry=entry,
        name=name,
        url=url,
        thumbnail=thumbnail,
    )
    return query
