from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Query, Router
from ninja.pagination import paginate

from .filters import ProducerFilter
from .models import ProducerModel
from .schemas import ProducerSchema

router = Router(tags=["producers"])


@router.get("", response=list[ProducerSchema])
@paginate
def get_producer_info(request: HttpRequest, filters: ProducerFilter = Query(...)):
    query_object = Q()
    query_dict = filters.dict(exclude_none=True)

    character_name = query_dict.pop("name", None)
    if character_name:
        query = Q()
        for position in character_name.split(","):
            query |= Q(**{f"name__icontains": position.strip()})
        query_object &= query

    query = ProducerModel.objects.all()

    if query_object:
        query = query.filter(query_object).distinct()

    return query


@router.get("/{str:producer_id}/", response=ProducerSchema)
def get_individual_character_info(request: HttpRequest, producer_id: str):
    queryset = get_object_or_404(ProducerModel, id=producer_id)
    return queryset
