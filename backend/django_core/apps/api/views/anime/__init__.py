import datetime

from apps.anime.models import AnimeModel, AnimeNameSynonymModel
from apps.anime.models.anime_genre import AnimeGenreModel
from apps.anime.models.anime_theme import AnimeThemeModel
from apps.api.auth import AuthBearer
from apps.api.decorator import permission_required
from apps.api.filters.anime import AnimeInfoFilters
from apps.api.permissions import IsSuperUser
from apps.characters.models import CharacterModel
from apps.producers.models import ProducerModel
from apps.staffs.models import StaffModel
from django.db.models import Q, QuerySet
from django.db.models.functions import Greatest
from django.http import Http404, HttpRequest
from django.shortcuts import get_object_or_404
from ninja import File, Form, Query, Router, UploadedFile
from ninja.pagination import paginate

try:
    from django.contrib.postgres.search import TrigramSimilarity

    HAS_POSTGRES = True
except ImportError:
    HAS_POSTGRES = False

from ...schemas.anime import AnimeInfoGETSchema

router = Router()


@router.get("", response=list[AnimeInfoGETSchema])
@paginate
def get_anime_info(
    request: HttpRequest,
    filters: AnimeInfoFilters = Query(...),
) -> QuerySet[AnimeModel]:
    if not HAS_POSTGRES:
        raise Http404("Looksups are not supported on any other databases except Postgres")

    query_dict = filters.dict(exclude_none=True)
    query_object = Q()
    # 2 Step get query
    # There wont be a performance hit if we do all().filter()
    # https://docs.djangoproject.com/en/4.0/topics/db/queries/#retrieving-specific-objects-with-filters
    query = AnimeModel.objects.all()

    # We must pop this to filter other fields on the later stage
    if name := query_dict.pop("name", None):
        query = (
            query.annotate(
                similiarity=Greatest(
                    TrigramSimilarity("name", name),
                    TrigramSimilarity("name_japanese", name),
                    TrigramSimilarity("name_synonyms__name", name),
                )
            )
            .filter(
                similiarity__gte=0.3,
            )
            .order_by("-similiarity")
        )

    # Same here but with ids
    for id in [
        "mal_id",
        "kitsu_id",
        "anilist_id",
    ]:
        if value := query_dict.pop(id, None):
            _query_ = Q()
            for position in str(value).split(","):
                _query_ |= Q(
                    **{f"{id}": int(position.strip())},
                )
            query_object &= _query_

    # Staff lookups
    if staff := query_dict.pop("staffs", None):
        for position in staff.split(","):
            _query_ &= (
                Q(staff__name__icontains=position.strip())
                | Q(
                    staff__alternate_names__name__icontains=position.strip(),
                )
                | Q(staff__family_name__icontains=position.strip())
                | Q(staff__family_name__icontains=position.strip())
            )
            query_object &= _query_

    # Many to many lookups

    for item in [
        "genres",
        "themes",
        "studios",
        "producers",
        "characters",
    ]:
        if value := query_dict.pop(item, None):
            _query_ = Q()
            for position in value.split(","):
                _query_ &= Q(
                    **{f"{item}__name__icontains": position.strip()},
                )
            query_object &= _query_

    # This can be (AND: )
    # This means it is empty

    if query_object:
        query = query.filter(query_object).distinct()

    if not query:
        raise Http404(
            "No {} matches the given query with {}".format(
                query.model._meta.object_name,
                query_object,
            )
        )
    return query


@router.post("", response=AnimeInfoGETSchema, auth=AuthBearer())
@permission_required([IsSuperUser])
def post_anime_info(
    request: HttpRequest,
    mal_id: int | None = Form(default=None),
    anilist_id: int | None = Form(default=None),
    kitsu_id: int | None = Form(default=None),
    name: str = Form(..., max_length=1024),
    name_japanese: str | None = Form(default=None, max_length=1024),
    name_synonyms: list[str] = Form(default=None),
    source: str | None = Form(default=None),
    aired_from: datetime.datetime | None = Form(default=None),
    aired_to: datetime.datetime | None = Form(default=None),
    synopsis: str | None = Form(default=None),
    background: str | None = Form(default=None),
    rating: str | None = Form(default=None),
    # Images
    banner: UploadedFile | None = File(default=None),
    cover: UploadedFile | None = File(default=None),
    # We need pk for these
    staffs: list[str] = Form(default=None),
    genres: list[str] = Form(default=None),
    themes: list[str] = Form(default=None),
    studios: list[str] = Form(default=None),
    producers: list[str] = Form(default=None),
    characters: list[str] = Form(default=None),
) -> AnimeModel:
    kwargs = {
        "mal_id": mal_id,
        "anilist_id": anilist_id,
        "kitsu_id": kitsu_id,
        "name": name,
        "name_japanese": name_japanese,
        "source": source,
        "aired_from": aired_from,
        "aired_to": aired_to,
        "banner": banner,
        "cover": cover,
        "synopsis": synopsis,
        "background": background,
        "rating": rating,
        # m2m Fields
        "staffs": staffs[0].split(",") if staffs else None,
        "genres": genres[0].split(",") if genres else None,
        "themes": themes[0].split(",") if themes else None,
        "studios": studios[0].split(",") if studios else None,
        "producers": producers[0].split(",") if producers else None,
        "characters": characters[0].split(",") if producers else None,
        #   synonyms names can be
        #       like this   :   ['hello,world']
        #   What we want is :   ['hello', 'world']
        "name_synonyms": name_synonyms[0].split(",") if name_synonyms else None,
    }

    model_data = {
        key: value
        for key, value in kwargs.items()
        if key
        not in [
            # Ignore M2M relations
            "name_synonyms",
            "genres",
            "themes",
            "studios",
            "producers",
            "characters",
        ]
        and value
        not in [
            None,
            "",  # ignore empty strings
            0,
        ]
    }
    database = AnimeModel.objects.create(**model_data)

    if name_synonyms_list := kwargs.get("name_synonyms", None):
        for anime_name_synonym in name_synonyms_list:
            anime_synonym_instance, _ = AnimeNameSynonymModel.objects.get_or_create(
                name=anime_name_synonym.strip(),
            )
            database.name_synonyms.add(anime_synonym_instance)

    if genres_list := kwargs.get("genres", None):
        for genre in genres_list:
            genre_instance = AnimeGenreModel.objects.get(pk=genre)
            database.genres.add(genre_instance)

    if themes_list := kwargs.get("themes", None):
        for theme in themes_list:
            theme_instance = AnimeThemeModel.objects.get(pk=theme)
            database.themes.add(theme_instance)

    if studios_list := kwargs.get("studios", None):
        for studio in studios_list:
            studio_instance = ProducerModel.objects.get(pk=studio)
            database.studios.add(studio_instance)

    if producers_list := kwargs.get("producers", None):
        for producer in producers_list:
            producer_instance = ProducerModel.objects.get(pk=producer)
            database.producers.add(producer_instance)

    if characters_list := kwargs.get("characters", None):
        for character in characters_list:
            character_instance = CharacterModel.objects.get(pk=character)
            database.characters.add(character_instance)

    if staffs_list := kwargs.get("staffs", None):
        for staff in staffs_list:
            staff_instance = StaffModel.objects.get(pk=staff)
            database.staffs.add(staff_instance)

    return database


@router.get("/{int:anime_id}", response=AnimeInfoGETSchema)
def get_individual_anime_info(
    request: HttpRequest,
    anime_id: int,
) -> AnimeModel:
    query = get_object_or_404(AnimeModel, pk=anime_id)
    return query


@router.patch("/{int:anime_id}", response=AnimeInfoGETSchema, auth=AuthBearer())
@permission_required([IsSuperUser])
def patch_individual_anime_info(
    request: HttpRequest,
    anime_id: int,
    # Optional parameters
    mal_id: int | None = Form(default=None),
    anilist_id: int | None = Form(default=None),
    kitsu_id: int | None = Form(default=None),
    name: str | None = Form(None, max_length=1024),
    name_japanese: str | None = Form(default=None, max_length=1024),
    name_synonyms: list[str] = Form(default=None),
    source: str | None = Form(default=None),
    aired_from: datetime.datetime | None = Form(default=None),
    aired_to: datetime.datetime | None = Form(default=None),
    synopsis: str | None = Form(default=None),
    background: str | None = Form(default=None),
    rating: str | None = Form(default=None),
    # Images
    banner: UploadedFile | None = File(default=None),
    cover: UploadedFile | None = File(default=None),
    # We need pk for these
    staffs: list[str] = Form(default=None),
    genres: list[str] = Form(default=None),
    themes: list[str] = Form(default=None),
    studios: list[str] = Form(default=None),
    producers: list[str] = Form(default=None),
    characters: list[str] = Form(default=None),
) -> AnimeModel:
    kwargs = {
        "mal_id": mal_id,
        "anilist_id": anilist_id,
        "kitsu_id": kitsu_id,
        "name": name,
        "name_japanese": name_japanese,
        "source": source,
        "aired_from": aired_from,
        "aired_to": aired_to,
        "banner": banner,
        "cover": cover,
        "synopsis": synopsis,
        "background": background,
        "rating": rating,
    }
    # Filter and remove the None values
    filtered_kwargs = {key: value for key, value in kwargs.items() if value}

    instance = get_object_or_404(AnimeModel, pk=anime_id)
    for attribute, value in filtered_kwargs.items():
        setattr(instance, attribute, value)

    # Work with m2m fields
    m2m_kwargs = {
        "staffs": staffs[0].split(",") if staffs else None,
        "genres": genres[0].split(",") if genres else None,
        "themes": themes[0].split(",") if themes else None,
        "studios": studios[0].split(",") if studios else None,
        "producers": producers[0].split(",") if producers else None,
        "characters": characters[0].split(",") if producers else None,
        #   synonyms names can be
        #       like this   :   ['hello,world']
        #   What we want is :   ['hello', 'world']
        "name_synonyms": name_synonyms[0].split(",") if name_synonyms else None,
    }
    filtered_m2m_kwargs = {key: value for key, value in m2m_kwargs.items() if value}

    for attribute, value in filtered_m2m_kwargs.items():
        if specific_field := getattr(instance, attribute):
            specific_field.set(value)

    instance.save()
    return instance
