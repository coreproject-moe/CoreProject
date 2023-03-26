from django.http import JsonResponse, HttpRequest

# Import our models here
from apps.anime.models import AnimeModel
from apps.characters.models import CharacterModel
from apps.producers.models import ProducerModel
from apps.staffs.models import StaffModel

# Create your views here.


def all_anime_ids(request: HttpRequest) -> JsonResponse:
    query = AnimeModel.objects.all().values_list("pk", flat=True)
    return JsonResponse({"data": list(query)})


def all_character_ids(request: HttpRequest) -> JsonResponse:
    query = CharacterModel.objects.all().values_list("pk", flat=True)
    return JsonResponse({"data": list(query)})


def all_producer_ids(request: HttpRequest) -> JsonResponse:
    query = ProducerModel.objects.all().values_list("pk", flat=True)
    return JsonResponse({"data": list(query)})


def all_staff_ids(request: HttpRequest) -> JsonResponse:
    query = StaffModel.objects.all().values_list("pk", flat=True)
    return JsonResponse({"data": list(query)})
