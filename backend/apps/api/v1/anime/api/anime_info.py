from django.db.models import Q
from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Query, Router

from ..filters import AnimeInfoFilters
from ..models import AnimeInfoModel
from ..schemas import AnimeInfoSchema

router = Router()


@router.get("/info", response=list[AnimeInfoSchema])
def get_anime_info(request, filters: AnimeInfoFilters = Query(...)):
    anime_genres = filters.dict(exclude_none=True).get("anime_genres", "").split(",")
    anime_themes = filters.dict(exclude_none=True).get("anime_themes", "").split(",")

    query = get_list_or_404(
        AnimeInfoModel,
        Q(anime_genres__name__in=[anime_genres][0]),
        Q(anime_themes__name__in=[anime_themes][0]),
        Q(
            **{
                i: filters.dict(exclude_none=True)[i]
                for i in filters.dict(exclude_none=True)
                if i != "anime_genres" and i != "anime_themes"
            }
        ),
    )
    return query


@router.get("/info/{int:anime_id}", response=AnimeInfoSchema)
def get_individual_anime_info(request, anime_id: int):
    query = get_object_or_404(AnimeInfoModel, id=anime_id)
    return query
