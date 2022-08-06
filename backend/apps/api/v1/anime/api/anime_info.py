from django.db.models import Q
from django.http import Http404, HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Query, Router
from ninja.pagination import paginate

from ..filters import AnimeInfoFilters
from ..models import AnimeInfoModel
from ..schemas import AnimeInfoGETSchema, AnimeInfoPOSTSchema

router = Router()


@router.get("/info", response=list[AnimeInfoGETSchema])
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

    # Dictionary unpacking at finest
    for item in query_dict:
        query = Q()
        for position in query_dict[item].split(","):
            query |= Q(**{f"{item}__name__icontains": position})
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


@router.post("/info", response=AnimeInfoGETSchema)
def post_anime_info(request: HttpRequest, payload: AnimeInfoPOSTSchema):
    instance = AnimeInfoModel.objects.create(**payload.dict())
    return instance


@router.get("/info/{int:anime_id}", response=AnimeInfoGETSchema)
def get_individual_anime_info(request: HttpRequest, anime_id: int):
    query = get_object_or_404(AnimeInfoModel, id=anime_id)
    return query
