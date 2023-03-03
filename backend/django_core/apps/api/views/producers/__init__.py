from http import HTTPStatus
from ninja import Query, Router
from ninja.pagination import paginate

from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404

from apps.user.models import CustomUser

from ...auth import AuthBearer

from ....producers.models import ProducerModel
from ...filters.producers import ProducerFilter
from ...schemas.producers import ProducerGETSchema, ProducerPOSTSchema

router = Router()


@router.get("", response=list[ProducerGETSchema])
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


@router.post("", response=ProducerGETSchema, auth=AuthBearer())
def post_producer_info(request: HttpRequest, payload: ProducerPOSTSchema) -> ProducerModel:
    user: CustomUser = request.auth
    if not user.is_superuser:
        raise HttpResponse(
            "Superuser is required for this operation", status=HTTPStatus.UNAUTHORIZED
        )
    ProducerModel.objects.get


@router.get("/{str:producer_id}/", response=ProducerGETSchema)
def get_individual_producer_info(
    request: HttpRequest,
    producer_id: str,
) -> ProducerModel:
    queryset = get_object_or_404(ProducerModel, pk=producer_id)
    return queryset
