from http import HTTPStatus

from apps.user.models import CustomUser
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from ninja import Query, Router
from ninja.pagination import paginate

from ....producers.models import ProducerModel
from ...auth import AuthBearer
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

    if character_name := query_dict.pop("name", None):
        _query_ = Q()
        for position in character_name.split(","):
            _query_ |= Q(**{"name__icontains": position.strip()})
        query_object &= _query_

    if mal_id := query_dict.pop("mal_id", None):
        _query_ = Q()
        for position in str(mal_id).split(","):
            _query_ |= Q(
                **{"mal_id": position.strip()},
            )
        query_object &= _query_

    query = ProducerModel.objects.all()

    if query_object:
        query = query.filter(query_object).distinct()

    return query


@router.post("", response=ProducerGETSchema, auth=AuthBearer())
def post_producer_info(request: HttpRequest, payload: ProducerPOSTSchema) -> ProducerModel:
    user: CustomUser = request.auth
    if not user.is_superuser:
        return HttpResponse(
            "Superuser is required for this operation", status=HTTPStatus.UNAUTHORIZED
        )

    instance = ProducerModel.objects.create(**payload.dict(exclude_none=True))
    return instance


@router.get("/{int:producer_id}/", response=ProducerGETSchema)
def get_individual_producer_info(
    request: HttpRequest,
    producer_id: int,
) -> ProducerModel:
    queryset = get_object_or_404(ProducerModel, pk=producer_id)
    return queryset


@router.patch("/{str:producer_id}/", response=ProducerGETSchema, auth=AuthBearer())
def patch_individual_producer_info(
    request: HttpRequest,
    producer_id: int,
    # Optional
    payload: ProducerPOSTSchema,
) -> ProducerModel:
    user: CustomUser = request.auth
    if not user.is_superuser:
        return HttpResponse(
            "Superuser is required for this operation",
            status=HTTPStatus.UNAUTHORIZED,
        )

    queryset = get_object_or_404(ProducerModel, pk=producer_id)
    for attribute, value in payload.dict(exclude_none=True):
        setattr(queryset, attribute, value)

    queryset.save()
    return queryset
