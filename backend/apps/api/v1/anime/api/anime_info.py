from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from ninja import Query, Router
from ninja.pagination import paginate

from ..filters import AnimeInfoFilters
from ..models import AnimeInfoModel
from ..schemas import AnimeInfoSchema

router = Router()


@router.get("/info", response=list[AnimeInfoSchema])
@paginate
def get_anime_info(request, filters: AnimeInfoFilters = Query(...)):
    query_dict = filters.dict(exclude_none=True)
    query_object = Q()

    # Django filters anyone?
    anime_name = query_dict.get("anime_name", None)
    if anime_name:
        query_object &= (
            Q(anime_name_japanese__icontains=anime_name)
            | Q(anime_name__icontains=anime_name)
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
            query |= Q(anime_producer__name__icontains=position)
        query_object &= query

    query = AnimeInfoModel.objects.filter(query_object)
    if not query:
        raise Http404("No %s matches the given query." % query.model._meta.object_name)

    return query


@router.get("/info/{int:anime_id}", response=AnimeInfoSchema)
def get_individual_anime_info(request, anime_id: int):
    query = get_object_or_404(AnimeInfoModel, id=anime_id)
    return query
