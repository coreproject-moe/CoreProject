from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Router, Query
from ninja.pagination import paginate

from .models import CharacterModel
from .schemas import CharacterSchema
from .filters import CharacterFilter

router = Router(tags=["characters"])


@router.get("", response=list[CharacterSchema])
@paginate
def get_character_info(request: HttpRequest, filter: CharacterFilter = Query(...)):
    query = CharacterModel.objects.all()
    return query


@router.get("/{str:character_id}/", response=CharacterSchema)
def get_individual_character_info(request: HttpRequest, character_id: str):
    queryset = get_object_or_404(CharacterModel, id=character_id)
    return queryset
