from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404

from .models import AnimeInfoModel
from .serializers import (
    AnimeInfoSerializer,
    EpisodeSerializer,
)

# Create your views here.


class AnimeInfoView(GenericViewSet, CreateModelMixin):
    """
    Returns :
        - All uploaded animes
        - Detailed info on uploaded animes
        - Detailed Episodes info
    """

    queryset = AnimeInfoModel.objects.all()
    serializer_class = AnimeInfoSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ["updated"]

    def list(self, request: HttpRequest) -> Response:
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request: HttpRequest, pk: int) -> Response:
        queryset = get_object_or_404(self.get_queryset(), id=pk)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    def post(self, request: HttpRequest) -> Response:
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    @action(detail=True)
    def episode(self, request, pk: int, episode_number: int = None) -> Response:
        queryset = get_object_or_404(self.get_queryset(), id=pk)

        if episode_number:
            queryset = queryset.episodes.get(episode_number=episode_number)
            serializer = EpisodeSerializer(queryset, many=False)
        else:
            queryset = queryset.episodes.all()
            serializer = EpisodeSerializer(queryset, many=True)

        return Response(data=serializer.data)
