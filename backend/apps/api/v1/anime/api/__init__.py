from django.db.models import Q
from django.http import Http404, HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Query, Router
from ninja.pagination import paginate

from ..filters import AnimeInfoFilters
from ..models import AnimeModel
from ..schemas import AnimeInfoGETSchema, AnimeInfoPOSTSchema

router = Router(tags=["anime_info"])


@router.get("", response=list[AnimeInfoGETSchema])
@paginate
def get_anime_info(request: HttpRequest, filters: AnimeInfoFilters = Query(...)):
    query_dict = filters.dict(exclude_none=True)
    query_object = Q()

    # We must pop this to filter other fields on the later stage
    anime_name = query_dict.pop("anime_name", None)
    if anime_name:
        query_object &= (
            Q(anime_name__icontains=anime_name)
            | Q(anime_name_japanese__icontains=anime_name)
            | Q(anime_name_synonyms__name__icontains=anime_name)
        )

    # Same here but with ids
    anime_lookups = (
        "mal_id",
        "kitsu_id",
        "anilist_id",
    )
    for item in anime_lookups:
        value = query_dict.pop(item, None)
        if value:
            query = Q()
            for position in value.split(","):
                query |= Q(**{f"{item}": int(position.strip())})
            query_object &= query

    # Many to many lookups
    m2m_lookups = (
        "anime_genres",
        "anime_themes",
        "anime_studios",
        "anime_producers",
        "anime_characters",
    )
    for item in m2m_lookups:
        value = query_dict.pop(item, None)
        if value:
            query = Q()
            for position in value.split(","):
                query &= Q(**{f"{item}__name__icontains": position.strip()})
            query_object &= query

    # 2 Step get query
    # There wont be a performance hit if we do all().filter()
    # https://docs.djangoproject.com/en/4.0/topics/db/queries/#retrieving-specific-objects-with-filters
    query = AnimeModel.objects.all()

    # This can be (AND: )
    # This means it is empty
    if query_object:
        query = query.filter(query_object).distinct()

    if not query:
        raise Http404(
            f"No {query.model._meta.object_name} matches the given query with {query_object}"
        )
    return query


@router.post("", response=AnimeInfoGETSchema)
def post_anime_info(request: HttpRequest, payload: AnimeInfoPOSTSchema):
    instance = AnimeModel.objects.create(**payload.dict())
    return instance


@router.get("/{int:anime_id}", response=AnimeInfoGETSchema)
def get_individual_anime_info(request: HttpRequest, anime_id: int):
    query = get_object_or_404(AnimeModel, id=anime_id)
    return query


# Router Configuration
# __ DO NOT MODIFY __

from .anime_character import router as anime_character_router
from .anime_genre import router as anime_genre_router
from .anime_producer import router as anime_producer_router
from .anime_studio import router as anime_studio_router
from .anime_theme import router as anime_theme_router

router.add_router("", anime_genre_router, tags=["anime_info"])
router.add_router("", anime_producer_router, tags=["anime_info"])
router.add_router("", anime_studio_router, tags=["anime_info"])
router.add_router("", anime_character_router, tags=["anime_info"])
router.add_router("", anime_theme_router, tags=["anime_info"])


from .episode import router as episode_router
from .episode_comment import router as episode_comment_router
from .episode_timestamp import router as episode_timestamp_router

router.add_router("", episode_router, tags=["anime_episodes"])
router.add_router("", episode_timestamp_router, tags=["anime_episodes"])
router.add_router("", episode_comment_router, tags=["anime_episodes"])
