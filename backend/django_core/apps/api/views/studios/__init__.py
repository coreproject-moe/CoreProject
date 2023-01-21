from ninja import Query, Router
from ninja.pagination import paginate

from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from ....studios.models import StudioModel
from ...filters.studios import StudioFilter
from ...schemas.studios import StudioSchema

router = Router()


@router.get("", response=list[StudioSchema])
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


@router.get("/{str:studio_id}/", response=StudioSchema)
def get_individual_studio_info(
    request: HttpRequest,
    studio_id: str,
) -> StudioModel:
    queryset = get_object_or_404(StudioModel, pk=studio_id)
    return queryset
