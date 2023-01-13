import contextlib
import datetime

from apps.anime.models import AnimeModel
from apps.anime.models.anime_genre import AnimeGenreModel
from apps.anime.models.anime_synonym import AnimeSynonymModel
from apps.anime.models.anime_theme import AnimeThemeModel
from apps.api.filters.anime import AnimeInfoFilters
from apps.characters.models import CharacterModel
from apps.producers.models import ProducerModel
from apps.studios.models import StudioModel
from ninja import File, Form, Query, Router
from ninja.files import UploadedFile
from ninja.pagination import paginate

from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.db.models import Q, QuerySet
from django.http import Http404, HttpRequest
from django.shortcuts import get_object_or_404

from ...schemas.anime import AnimeInfoGETSchema

router = Router()


@router.get("", response=list[AnimeInfoGETSchema])
@paginate
def get_anime_info(
    request: HttpRequest,
    filters: AnimeInfoFilters = Query(...),
) -> QuerySet[AnimeModel]:
    query_dict = filters.dict(exclude_none=True)
    query_object = Q()
    # 2 Step get query
    # There wont be a performance hit if we do all().filter()
    # https://docs.djangoproject.com/en/4.0/topics/db/queries/#retrieving-specific-objects-with-filters
    query = AnimeModel.objects.all()

    # We must pop this to filter other fields on the later stage
    anime_name = query_dict.pop("anime_name", None)
    if anime_name:
        _vector_ = SearchVector(
            "anime_name",
            "anime_name_japanese",
            "anime_name_synonyms__name",
        )
        _query_ = SearchQuery(anime_name)
        query = query.annotate(
            anime_name_rank=SearchRank(
                _vector_,
                _query_,
            )
        ).order_by("-anime_name_rank")

    # Same here but with ids
    id_lookups = [
        "mal_id",
        "kitsu_id",
        "anilist_id",
    ]
    for id in id_lookups:
        value = query_dict.pop(id, None)
        if value:
            _query_ = Q()
            for position in value.split(","):
                _query_ |= Q(
                    **{f"{id}": int(position.strip())},
                )
            query_object &= _query_

    # Many to many lookups
    m2m_lookups = [
        "anime_genres",
        "anime_themes",
        "anime_studios",
        "anime_producers",
        "anime_characters",
    ]
    for item in m2m_lookups:
        value = query_dict.pop(item, None)
        if value:
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


@router.post("", response=AnimeInfoGETSchema)
def post_anime_info(
    request: HttpRequest,
    mal_id: int | None = Form(default=None),
    anilist_id: int | None = Form(default=None),
    kitsu_id: int | None = Form(default=None),
    anime_name: str = Form(..., max_length=1024),
    anime_name_japanese: str | None = Form(default=None, max_length=1024),
    anime_name_synonyms: list[str] = Form(default=None),
    anime_source: str | None = Form(default=None),
    anime_aired_from: datetime.datetime | None = Form(default=None),
    anime_aired_to: datetime.datetime | None = Form(default=None),
    anime_banner: UploadedFile | None = File(default=None),
    anime_cover: UploadedFile | None = File(default=None),
    anime_synopsis: str | None = Form(default=None),
    anime_background: str | None = Form(default=None),
    anime_rating: str | None = Form(default=None, max_length=50),
    anime_genres: list[str] = Form(default=None),
    anime_themes: list[str] = Form(default=None),
    anime_studios: list[str] = Form(default=None),
    anime_producers: list[str] = Form(default=None),
    anime_characters: list[str] = Form(default=None),
) -> AnimeModel:
    kwargs = {
        "mal_id": mal_id,
        "anilist_id": anilist_id,
        "kitsu_id": kitsu_id,
        "anime_name": anime_name,
        "anime_name_japanese": anime_name_japanese,
        "anime_name_synonyms": anime_name_synonyms,
        "anime_source": anime_source,
        "anime_aired_from": anime_aired_from,
        "anime_aired_to": anime_aired_to,
        "anime_banner": anime_banner,
        "anime_cover": anime_cover,
        "anime_synopsis": anime_synopsis,
        "anime_background": anime_background,
        "anime_rating": anime_rating,
        "anime_genres": anime_genres,
        "anime_themes": anime_themes,
        "anime_studios": anime_studios,
        "anime_producers": anime_producers,
        "anime_characters": anime_characters,
    }

    model_data = {
        key: value
        for key, value in kwargs.items()
        if key
        not in [
            # Ignore M2M relations
            "anime_name_synonyms",
            "anime_genres",
            "anime_themes",
            "anime_studios",
            "anime_producers",
            "anime_characters",
        ]
        and value
        not in [
            None,
            "",  # ignore empty strings
            0,
        ]
    }
    anime_model_instance, _ = AnimeModel.objects.get_or_create(
        anime_name=kwargs["anime_name"],
        defaults=model_data,
    )
    
    if anime_name_synonym_list := kwargs.get("anime_name_synonyms", None):
        anime_name_synonym_m2m_list: list[AnimeSynonymModel] = []

        for anime_name_synonym in anime_name_synonym_list[0].split(","):
            anime_synonym_instance, _ = AnimeSynonymModel.objects.get_or_create(
                name=anime_name_synonym.strip(),
            )
            anime_name_synonym_m2m_list.append(anime_synonym_instance)

        anime_model_instance.anime_name_synonyms.add(*anime_name_synonym_m2m_list)

    if anime_genres_list := kwargs.get("anime_genres", None):
        anime_genre_m2m_list: list[AnimeGenreModel] = []

        for anime_genre in anime_genres_list[0].split(","):
            with contextlib.suppress(AnimeGenreModel.DoesNotExist):
                anime_genre_instance = AnimeGenreModel.objects.get(
                    name=anime_genre.strip(),
                )
                anime_genre_m2m_list.append(anime_genre_instance)

        anime_model_instance.anime_genres.add(*anime_genre_m2m_list)

    if anime_themes_list := kwargs.get("anime_themes", None):
        anime_theme_m2m_list: list[AnimeThemeModel] = []

        for anime_theme in anime_themes_list[0].split(","):
            with contextlib.suppress(AnimeThemeModel.DoesNotExist):
                anime_theme_instance = AnimeThemeModel.objects.get(
                    name=anime_theme.strip(),
                )
                anime_theme_m2m_list.append(anime_theme_instance)

        anime_model_instance.anime_themes.add(*anime_theme_m2m_list)

    if anime_studios_list := kwargs.get("anime_studios", None):
        anime_studio_m2m_list: list[StudioModel] = []

        for anime_studio in anime_studios_list[0].split(","):
            with contextlib.suppress(StudioModel.DoesNotExist):
                anime_studio_instance = StudioModel.objects.get(
                    name=anime_studio.strip(),
                )
                anime_studio_m2m_list.append(anime_studio_instance)

        anime_model_instance.anime_studios.add(*anime_studio_m2m_list)

    if anime_producers_list := kwargs.get("anime_producers", None):
        anime_producer_m2m_list: list[ProducerModel] = []

        for anime_producer in anime_producers_list[0].split(","):
            with contextlib.suppress(ProducerModel.DoesNotExist):
                anime_producer_instance = ProducerModel.objects.get(
                    name=anime_producer.strip(),
                )
                anime_producer_m2m_list.append(anime_producer_instance)

        anime_model_instance.anime_producers.add(*anime_producer_m2m_list)

    if anime_characters_list := kwargs.get("anime_characters", None):
        anime_characters_m2m_list: list[CharacterModel] = []

        for anime_character in anime_characters_list[0].split(","):
            with contextlib.suppress(CharacterModel.DoesNotExist):
                anime_character_instance = CharacterModel.objects.get(
                    name=anime_character.strip(),
                )
                anime_characters_m2m_list.append(anime_character_instance)

        anime_model_instance.anime_characters.add(*anime_characters_m2m_list)

    return anime_model_instance


@router.get("/{int:anime_id}", response=AnimeInfoGETSchema)
def get_individual_anime_info(
    request: HttpRequest,
    anime_id: int,
) -> AnimeModel:
    query = get_object_or_404(AnimeModel, id=anime_id)
    return query
