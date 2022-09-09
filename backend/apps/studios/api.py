from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Query, Router
from ninja.pagination import paginate

from .filters import StudioFilter
from .models import StudioModel
from .schemas import StudioSchema

router = Router(tags=["studios"])


@router.get("", response=list[StudioSchema])
@paginate
def get_studio_info(request: HttpRequest, filters: StudioFilter = Query(...)):
    query_object = Q()
    query_dict = filters.dict(exclude_none=True)

    character_name = query_dict.pop("name", None)
    if character_name:
        query = Q()
        for position in character_name.split(","):
            query |= Q(**{"name__icontains": position.strip()})
        query_object &= query

    query = StudioModel.objects.all().filter()

    if query_object:
        query = query.filter(query_object).distinct()

    return query


@router.get("/{str:studio_id}/", response=StudioSchema)
def get_individual_studio_info(request: HttpRequest, studio_id: str):
    queryset = get_object_or_404(StudioModel, id=studio_id)
    return queryset
