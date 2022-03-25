from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.parsers import (
    FormParser,
    MultiPartParser,
    JSONParser,
)

from .permissions import IsSuperUserOrReadOnly
from .models import AnimeInfoModel
from .serializers import (
    AnimeInfoSerializer,
    EpisodeSerializer,
)

# Create your views here.


class AnimeInfoView(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
):
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
    parser_classes = [FormParser, MultiPartParser, JSONParser]
    permission_classes = [IsSuperUserOrReadOnly]

    @action(detail=True)
    def episode(
        self, request: HttpRequest, pk: int, episode_number: int = None
    ) -> Response:
        queryset = get_object_or_404(self.get_queryset(), pk=pk)

        if episode_number:
            queryset = queryset.episodes.get(episode_number=episode_number)
            serializer = EpisodeSerializer(queryset, many=False)
        else:
            queryset = queryset.episodes.all()
            serializer = EpisodeSerializer(queryset, many=True)

        return Response(data=serializer.data)

    @action(detail=True)
    def random(self, request: HttpRequest) -> Response:
        limit = request.GET.get("limit")
        queryset = self.get_queryset().order_by("?")[: int(limit)]
        serializer = self.get_serializer(queryset, many=True)

        return Response(data=serializer.data)
