from rest_framework import viewsets
from rest_framework.response import Response

from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404

from .models import AnimeInfoModel
from .serializers import AnimeInfoSerializer

# Create your views here.


class AnimeInfoView(viewsets.ViewSet):
    """
    Returns all uploaded animes and their detailed view
    """

    def list(self, request: HttpRequest) -> Response:
        queryset = AnimeInfoModel.objects.all()
        serializer = AnimeInfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request: HttpRequest, pk: int) -> Response:
        queryset = AnimeInfoModel.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = AnimeInfoSerializer(user)
        return Response(serializer.data)
