from django.http.request import HttpRequest
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.parsers import (
    FormParser,
    MultiPartParser,
    JSONParser,
)

from .filters import AnimeInfoFilter
from .permissions import IsSuperUserOrReadOnly
from .models import AnimeInfoModel, EpisodeModel
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
    UpdateModelMixin,
):
    """
    Returns :
        - All uploaded animes
        - Detailed info on uploaded animes
        - Detailed Episodes info
    """

    queryset = AnimeInfoModel.objects.all()
    serializer_class = AnimeInfoSerializer

    ordering_fields = ["updated"]
    parser_classes = [
        FormParser,
        MultiPartParser,
        JSONParser,
    ]
    permission_classes = [
        IsSuperUserOrReadOnly,
    ]
    filter_backends = [
        # SearchFilter,
        # OrderingFilter,
        DjangoFilterBackend,
    ]
    filter_class = AnimeInfoFilter
    # search_fields = ["anime_name", "anime_name_japanese"]

    def get_serializer_context(self):
        # Thanks StackOverFlow
        # https://stackoverflow.com/questions/31038742/pass-request-context-to-serializer-from-viewset-in-django-rest-framework
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    @action(detail=True)
    def random(self, request: HttpRequest) -> Response:
        limit = request.GET.get("limit")
        queryset = self.get_queryset().order_by("?")[: int(limit)]
        serializer = self.get_serializer(queryset, many=True)

        return Response(data=serializer.data)


class EpisodeView(
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    """
    Returns :
        - Detailed Episodes info
    """

    queryset = EpisodeModel.objects.all()
    serializer_class = EpisodeSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    lookup_field = "episode_number"  # https://stackoverflow.com/questions/61452449/how-to-change-lookup-field-in-model-viewset-to-other-unique-parameter-in-django

    def get_serializer_context(self):
        # Thanks StackOverFlow
        # https://stackoverflow.com/questions/31038742/pass-request-context-to-serializer-from-viewset-in-django-rest-framework
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
