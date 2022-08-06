from django.db.models import Q
from django.http import Http404, HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Query, Router
from ninja.pagination import paginate

from ..filters import AnimeInfoFilters
from ..models import AnimeInfoModel
from ..schemas import AnimeInfoPOSTSchema, AnimeInfoGETSchema

router = Router()


@router.get("/info", response=list[AnimeInfoGETSchema])
@paginate
def get_anime_info(request: HttpRequest, filters: AnimeInfoFilters = Query(...)):
    query_dict = filters.dict(exclude_none=True)
    query_object = Q()

    # Django filters anyone?
    anime_name = query_dict.get("anime_name", None)
    if anime_name:
        query_object &= (
            Q(anime_name__icontains=anime_name)
            | Q(anime_name_japanese__icontains=anime_name)
            | Q(anime_name_synonyms__name__icontains=anime_name)
        )

    anime_genres = query_dict.get("anime_genres", None)
    if anime_genres:
        query = Q()
        for position in anime_genres.split(","):
            query |= Q(anime_genres__name__icontains=position)
        query_object &= query

    anime_themes = query_dict.get("anime_themes", None)
    if anime_themes:
        query = Q()
        for position in anime_themes.split(","):
            query |= Q(anime_themes__name__icontains=position)
        query_object &= query

    anime_studios = query_dict.get("anime_studios", None)
    if anime_studios:
        query = Q()
        for position in anime_themes.split(","):
            query |= Q(anime_studios__name__icontains=position)
        query_object &= query

    anime_producer = query_dict.get("anime_producer", None)
    if anime_producer:
        query = Q()
        for position in anime_themes.split(","):
            query |= Q(anime_producers__name__icontains=position)
        query_object &= query

    # 2 Step get query
    # There wont be a performance hit if we do all().filter()
    # https://docs.djangoproject.com/en/4.0/topics/db/queries/#retrieving-specific-objects-with-filters
    query = AnimeInfoModel.objects.all()

    # This can be (AND: )
    # This means it is empty
    if query_object:
        query = query.filter(query_object).distinct()

    if not query:
        raise Http404(
            f"No {query.model._meta.object_name} matches the given query with {query_object}"
        )
    return query


@router.get("/info/{int:anime_id}", response=AnimeInfoGETSchema)
def get_individual_anime_info(request: HttpRequest, anime_id: int):
    query = get_object_or_404(AnimeInfoModel, id=anime_id)
    return query


@router.post("/info/{int:anime_id}", response=AnimeInfoGETSchema)
def post_individual_anime_info(
    request: HttpRequest, anime_id: int, payload: AnimeInfoPOSTSchema
):
    pass
