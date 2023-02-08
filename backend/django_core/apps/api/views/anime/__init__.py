import contextlib
import datetime

from apps.anime.models import AnimeModel, AnimeNameSynonymModel
from apps.anime.models.anime_genre import AnimeGenreModel
from apps.anime.models.anime_theme import AnimeThemeModel
from apps.api.filters.anime import AnimeInfoFilters
from apps.characters.models import CharacterModel
from apps.producers.models import ProducerModel
from apps.studios.models import StudioModel
from ninja import File, Form, Query, Router
from ninja.files import UploadedFile
from ninja.pagination import paginate

from django.db.models import Q, QuerySet
from django.db.models.functions import Greatest
from django.http import Http404, HttpRequest
from django.shortcuts import get_object_or_404

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

    print(query.explain(analyze=True))

    if not query:
        raise Http404(
            "No {} matches the given query with {}".format(
                query.model._meta.object_name,
                query_object,
            )
        )
    return query


@router.post("", response=AnimeInfoGETSchema)
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
    banner: UploadedFile | None = File(default=None),
    cover: UploadedFile | None = File(default=None),
    synopsis: str | None = Form(default=None),
    background: str | None = Form(default=None),
    rating: str | None = Form(default=None, max_length=50),
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
        "genres": genres,
        "themes": themes,
        "studios": studios,
        "producers": producers,
        "characters": characters,
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
    database, _ = AnimeModel.objects.get_or_create(
        name=kwargs["name"],
        defaults=model_data,
    )
    if name_synonyms_list := kwargs.get("name_synonyms", None):
        for anime_name_synonym in name_synonyms_list:
            anime_synonym_instance = AnimeNameSynonymModel.objects.create(
                name=anime_name_synonym.strip(),
            )
            database.name_synonyms.add(anime_synonym_instance)

    if genres_list := kwargs.get("genres", None):
        with contextlib.suppress(IndexError, AnimeGenreModel.DoesNotExist):
            for anime_genre in genres_list[0].split(","):
                anime_genre_instance = AnimeGenreModel.objects.get(
                    name=anime_genre.strip(),
                )
                database.genres.add(anime_genre_instance)

    if themes_list := kwargs.get("themes", None):
        with contextlib.suppress(IndexError, AnimeThemeModel.DoesNotExist):
            for anime_theme in themes_list[0].split(","):
                anime_theme_instance = AnimeThemeModel.objects.get(
                    name=anime_theme.strip(),
                )
                database.themes.add(anime_theme_instance)

    if studios_list := kwargs.get("studios", None):
        with contextlib.suppress(IndexError, StudioModel.DoesNotExist):
            for anime_studio in studios_list[0].split(","):
                anime_studio_instance = StudioModel.objects.get(
                    name=anime_studio.strip(),
                )
                database.studios.add(anime_studio_instance)

    if producers_list := kwargs.get("producers", None):
        with contextlib.suppress(IndexError, ProducerModel.DoesNotExist):
            for anime_producer in producers_list[0].split(","):
                anime_producer_instance = ProducerModel.objects.get(
                    name=anime_producer.strip(),
                )
                database.producers.add(anime_producer_instance)

    if characters_list := kwargs.get("characters", None):
        with contextlib.suppress(IndexError, CharacterModel.DoesNotExist):
            for anime_character in characters_list[0].split(","):
                anime_character_instance = CharacterModel.objects.get(
                    name=anime_character.strip(),
                )
                database.characters.add(anime_character_instance)

    return database


@router.get("/{int:anime_id}", response=AnimeInfoGETSchema)
def get_individual_anime_info(
    request: HttpRequest,
    anime_id: int,
) -> AnimeModel:
    query = get_object_or_404(AnimeModel, pk=anime_id)
    return query
