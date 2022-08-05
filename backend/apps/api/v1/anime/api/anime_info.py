from django.shortcuts import get_object_or_404
from ninja import Router, Query

from django.db.models import Q
from django.http import Http404
from ..models import AnimeInfoModel
from ..schemas import AnimeInfoSchema
from ..filters import AnimeInfoFilters

router = Router()


@router.get("/info", response=list[AnimeInfoSchema])
def get_anime_info(request, filters: AnimeInfoFilters = Query(...)):
    query_dict = filters.dict(exclude_none=True)
    query_object = Q()

    anime_name = query_dict.pop("anime_name", None)
    if anime_name:
        query_object &= (
            Q(anime_name_japanese__icontains=anime_name)
            | Q(anime_name__icontains=anime_name)
            | Q(anime_name_synonyms__name__icontains=anime_name)
        )
    # Django filters anyone?
    anime_genres = query_dict.pop("anime_genres", None)
    if anime_genres:
        query_object &= Q(anime_genres__name__in=anime_genres.split(","))

    anime_themes = query_dict.pop("anime_themes", None)
    if anime_themes:
        query_object &= Q(anime_themes__name__in=anime_themes.split(","))

    query = AnimeInfoModel.objects.filter(query_object, **query_dict).distinct()
    if not query:
        raise Http404("No %s matches the given query." % query.model._meta.object_name)

    return query


@router.get("/info/{int:anime_id}", response=AnimeInfoSchema)
def get_individual_anime_info(request, anime_id: int):
    query = get_object_or_404(AnimeInfoModel, id=anime_id)
    return query
