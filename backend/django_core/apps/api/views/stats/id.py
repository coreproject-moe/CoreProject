from apps.anime.models import AnimeModel
from apps.characters.models import CharacterModel
from apps.producers.models import ProducerModel
from apps.staffs.models import StaffModel
from django.http import HttpRequest
from ninja import Router

router = Router()


@router.get("/anime", response=list[int])
def get_all_anime_pk_from_db(request: HttpRequest) -> list[int]:
    query = AnimeModel.objects.all().values_list("pk", flat=True)
    return query


@router.get("/character", response=list[int])
def get_all_character_pk_from_db(request: HttpRequest) -> list[int]:
    query = CharacterModel.objects.all().values_list("pk", flat=True)
    return query


@router.get("/producer", response=list[int])
def get_all_producer_pk_from_db(request: HttpRequest) -> list[int]:
    query = ProducerModel.objects.all().values_list("pk", flat=True)
    return query


@router.get("/staff", response=list[int])
def get_all_staff_pk_from_db(request: HttpRequest):
    query = StaffModel.objects.all().values_list("pk", flat=True)
    return query
