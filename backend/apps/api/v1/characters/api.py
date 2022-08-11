from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Query, Router
from ninja.pagination import paginate

from .filters import CharacterFilter
from .models import CharacterModel
from .schemas import CharacterSchema

router = Router(tags=["characters"])


@router.get("", response=list[CharacterSchema])
@paginate
def get_character_info(request: HttpRequest, filters: CharacterFilter = Query(...)):
    query_object = Q()
    query_dict = filters.dict(exclude_none=True)

    character_name = query_dict.pop("name", None)
    if character_name:
        query = Q()
        for position in character_name.split(","):
            query |= Q(**{f"name__icontains": position.strip()})
        query_object &= query

    query = CharacterModel.objects.all()

    if query_object:
        query = query.filter(query_object).distinct()

    return query


@router.get("/{str:character_id}/", response=CharacterSchema)
def get_individual_character_info(request: HttpRequest, character_id: str):
    queryset = get_object_or_404(CharacterModel, id=character_id)
    return queryset
