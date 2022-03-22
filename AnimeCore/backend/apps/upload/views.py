from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404

from .models import AnimeInfoModel
from .serializers import AnimeInfoSerializer, EpisodeSerializer

# Create your views here.


class AnimeInfoView(viewsets.GenericViewSet):
    """
    Returns :
        - All uploaded animes
        - Detailed info on uploaded animes
        - Detailed Episodes info
    """

    queryset = AnimeInfoModel.objects.all()
    serializer_class = AnimeInfoSerializer

    def list(self, request: HttpRequest) -> Response:
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request: HttpRequest, pk: int) -> Response:
        queryset = get_object_or_404(self.get_queryset(), id=pk)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"])
    def episode(self, request, pk: int, episode_number: int = None) -> Response:
        queryset = get_object_or_404(self.get_queryset(), id=pk)

        if episode_number:
            queryset = queryset.episodes.get(episode_number=episode_number)
            serializer = EpisodeSerializer(queryset, many=False)
        else:
            queryset = queryset.episodes.all()
            serializer = EpisodeSerializer(queryset, many=True)

        return Response(data=serializer.data)
