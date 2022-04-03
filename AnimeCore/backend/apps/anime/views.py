from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
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
from .models import AnimeInfoModel
from .serializers import (
    AnimeInfoSerializer,
    EpisodeCommentSerializer,
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
    # https://stackoverflow.com/questions/61452449/how-to-change-lookup-field-in-model-viewset-to-other-unique-parameter-in-django
    lookup_field = "id"

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

    serializer_class = EpisodeSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    # https://stackoverflow.com/questions/61452449/how-to-change-lookup-field-in-model-viewset-to-other-unique-parameter-in-django
    lookup_field = "episode_number"

    def get_queryset(self):
        instance = AnimeInfoModel.objects.all()
        queryset = get_object_or_404(
            instance, pk=self.kwargs["anime_id"]
        ).anime_episodes.all()

        return queryset

    def get_serializer_context(self):
        # Thanks StackOverFlow
        # https://stackoverflow.com/questions/31038742/pass-request-context-to-serializer-from-viewset-in-django-rest-framework
        context = super().get_serializer_context()
        context.update(
            {"request": self.request},
        )
        return context


class EpisodeCommentView(
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    """
    Returns :
        - Comments
    """

    serializer_class = EpisodeCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        instance = AnimeInfoModel.objects.all()
        queryset = (
            get_object_or_404(
                instance,
                pk=self.kwargs["anime_id"],
            )
            .anime_episodes.get(
                episode_number__in=self.kwargs["episodes_episode_number"]
            )
            .episode_comments.all()
        )

        return queryset

    def get_serializer_context(self):
        # Thanks StackOverFlow
        # https://stackoverflow.com/questions/31038742/pass-request-context-to-serializer-from-viewset-in-django-rest-framework
        context = super().get_serializer_context()
        context.update(
            {"request": self.request},
        )
        return context
