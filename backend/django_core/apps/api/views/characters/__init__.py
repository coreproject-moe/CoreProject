
from apps.api.auth import AuthBearer
from apps.api.decorator import permission_required
from apps.api.permissions import IsSuperUser
from apps.characters.models import CharacterModel
from django.db.models import Q, QuerySet
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import File, Form, Query, Router
from ninja.files import UploadedFile
from ninja.pagination import paginate

try:
    from django.contrib.postgres.search import TrigramSimilarity

    HAS_POSTGRES = True
except ImportError:
    HAS_POSTGRES = False

from django.http import Http404

from ...filters.characters import CharacterFilter
from ...schemas.characters import CharacterSchema

router = Router()


@router.get("", response=list[CharacterSchema])
@paginate
def get_character_info(
    request: HttpRequest,
    filters: CharacterFilter = Query(...),
) -> QuerySet[CharacterModel]:
    if not HAS_POSTGRES:
        raise Http404("Looksups are not supported on any other databases except Postgres")

    query_object = Q()
    query_dict = filters.dict(exclude_none=True)
    query = CharacterModel.objects.all()

    character_name = query_dict.pop("name", None)
    if character_name:
        query = query.annotate(
            similarity=TrigramSimilarity("name", character_name)
        ).order_by("-similarity")

    # Same here but with ids
    id_lookups = [
        "mal_id",
        "kitsu_id",
        "anilist_id",
    ]
    for id in id_lookups:
        if value := query_dict.pop(id, None):
            _query_ = Q()
            for position in str(value).split(","):
                _query_ |= Q(**{f"{id}": int(position.strip())})
            query_object &= _query_

    if query_object:
        query = query.filter(query_object).distinct()

    return query


@router.post("", response=CharacterSchema, auth=AuthBearer())
@permission_required([IsSuperUser])
def post_character_info(
    request: HttpRequest,
    mal_id: int = Form(default=None),
    kitsu_id: int | None = Form(default=None),
    anilist_id: int | None = Form(default=None),
    name: str = Form(..., max_length=1024),
    name_kanji: str | None = Form(default=None, max_length=1024),
    character_image: UploadedFile | None = File(default=None),
    about: str | None = Form(default=None),
) -> QuerySet[CharacterModel]:
    instance = CharacterModel.objects.create(
        name=name,
        mal_id=mal_id,
        kitsu_id=kitsu_id,
        anilist_id=anilist_id,
        name_kanji=name_kanji,
        character_image=character_image,
        about=about,
    )
    return instance


@router.get("/{int:character_id}/", response=CharacterSchema)
def get_individual_character_info(
    request: HttpRequest,
    character_id: int,
) -> QuerySet[CharacterModel]:
    queryset = get_object_or_404(CharacterModel, pk=character_id)
    return queryset


@router.patch("/{int:character_id}/", response=CharacterSchema, auth=AuthBearer())
@permission_required([IsSuperUser])
def patch_individual_character_info(
    request: HttpRequest,
    character_id: int,
    # Optional fields
    mal_id: int = Form(default=None),
    kitsu_id: int | None = Form(default=None),
    anilist_id: int | None = Form(default=None),
    name: str = Form(None, max_length=1024),
    name_kanji: str | None = Form(default=None, max_length=1024),
    character_image: UploadedFile | None = File(default=None),
    about: str | None = Form(default=None),
):
    instance = get_object_or_404(CharacterModel, pk=character_id)

    kwargs = {
        "mal_id": mal_id,
        "kitsu_id": kitsu_id,
        "anilist_id": anilist_id,
        "name": name,
        "name_kanji": name_kanji,
        "character_image": character_image,
        "about": about,
    }
    filtered_kwargs = {key: value for key, value in kwargs.items() if value}
    for attribute, value in filtered_kwargs:
        setattr(instance, attribute, value)

    instance.save()
    return instance
