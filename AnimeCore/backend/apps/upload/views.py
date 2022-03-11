from rest_framework import generics
from rest_framework.response import Response

from django.http.request import HttpRequest
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from .models import AnimeInfoModel
from .serializers import AnimeInfoSerializer

# Create your views here.


class AnimeInfoView(generics.ListCreateAPIView):
    serializer_class = AnimeInfoSerializer

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request: HttpRequest, pk: int) -> Response:
        data = AnimeInfoModel.objects.get(id=pk)
        serializer = self.get_serializer(data)
        return Response(serializer.data)
