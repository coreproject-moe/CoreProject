from django.http import JsonResponse

from apps.anime.models import AnimeModel

# Create your views here.


def all_anime_ids(request):
    query = AnimeModel.objects.all().values_list("pk", flat=True)
    return JsonResponse({"data": list(query)})
