from http import HTTPStatus
from apps.api.auth import AuthBearer
from ninja import Query, Router
from ninja.pagination import paginate

from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404

from ....studios.models import StudioModel
from ...filters.studios import StudioFilter
from ...schemas.studios import StudioGETSchema, StudioPOSTSchema
from ....user.models import CustomUser

router = Router()


@router.get("", response=list[StudioGETSchema])
@paginate
def get_studio_info(
    request: HttpRequest,
    filters: StudioFilter = Query(...),
) -> StudioModel:
    query_object = Q()
    query_dict = filters.dict(exclude_none=True)

    if character_name := query_dict.pop("name", None):
        _query_ = Q()
        for position in character_name.split(","):
            _query_ |= Q(**{"name__icontains": position.strip()})
        query_object &= _query_

    query = StudioModel.objects.all()

    if query_object:
        query = query.filter(query_object).distinct()

    return query


@router.post("", response=StudioGETSchema, auth=AuthBearer())
def post_studio_info(request: HttpRequest, payload: StudioPOSTSchema) -> StudioModel:
    user: CustomUser = request.auth
    if not user.is_superuser:
        return HttpResponse(
            "Superuser is required for this operation", status=HTTPStatus.UNAUTHORIZED
        )

    instance = StudioModel.objects.create(**payload.dict(exclude_none=True))
    return instance


@router.get("/{str:studio_id}/", response=StudioGETSchema, auth=AuthBearer())
def get_individual_studio_info(
    request: HttpRequest,
    studio_id: str,
) -> StudioModel:
    queryset = get_object_or_404(StudioModel, pk=studio_id)
    return queryset
