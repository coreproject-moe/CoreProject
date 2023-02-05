from ninja import Query, Router
from ninja.pagination import paginate

from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from ....producers.models import ProducerModel
from ...filters.producers import ProducerFilter
from ...schemas.producers import ProducerSchema

router = Router()


@router.get("", response=list[ProducerSchema])
@paginate
def get_producer_info(
    request: HttpRequest,
    filters: ProducerFilter = Query(...),
) -> ProducerModel:
    query_object = Q()
    query_dict = filters.dict(exclude_none=True)

    character_name = query_dict.pop("name", None)
    if character_name:
        _query_ = Q()
        for position in character_name.split(","):
            _query_ |= Q(**{"name__icontains": position.strip()})
        query_object &= _query_

    query = ProducerModel.objects.all()

    if query_object:
        query = query.filter(query_object).distinct()

    return query


@router.get("/{str:producer_id}/", response=ProducerSchema)
def get_individual_producer_info(
    request: HttpRequest,
    producer_id: str,
) -> ProducerModel:
    queryset = get_object_or_404(ProducerModel, pk=producer_id)
    return queryset
