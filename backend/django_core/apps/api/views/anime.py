from apps.anime.models import AnimeModel
from apps.anime.models.anime_genre import AnimeGenreModel
from apps.anime.models.anime_theme import AnimeThemeModel
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from ..filters.anime import AnimeFilter
from ..serializers.anime import (
    AnimeGenreSerializer,
    AnimeGETSerializer,
    AnimePOSTSerializer,
    AnimeThemeSerializer,
)
from ..serializers.character import CharacterSerializer
from ..serializers.episode import EpisodeSerializer
from ..serializers.producer import ProducerSerializer
from ..serializers.staff import StaffSerializer

from rest_framework import exceptions


class AnimeViewSet(
    viewsets.GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):
    filter_backends = [DjangoFilterBackend]
    filter_class = AnimeFilter
    filterset_fields = ("name",)
    serializer_class = AnimePOSTSerializer
    queryset = AnimeModel.objects.all()
    lookup_field = "pk"
    # Capture only integers
    lookup_value_regex = "\d+"

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "list":
            return AnimeGETSerializer

        elif self.action == "anime_genres":
            return AnimeGenreSerializer

        elif self.action == "anime_themes":
            return AnimeThemeSerializer
        return AnimePOSTSerializer

    @action(
        detail=False,
        methods=["GET", "POST", "PUT"],
        filter_backends=[],
        serializer_class=AnimeThemeSerializer,
        url_path=r"themes(/(?P<theme_pk>\d+))?/?",
    )
    def anime_themes(self, *args, **kwargs):
        if self.request.method == "GET":
            query = AnimeGenreModel.objects.filter(type="anime")

            if theme_pk := kwargs.get("theme_pk"):
                query = get_object_or_404(query, pk=theme_pk)
                serializer = AnimeGenreSerializer(instance=query)
            else:
                serializer = AnimeGenreSerializer(instance=query, many=True)
            return Response(serializer.data)

        elif self.request.method == "POST":
            serializer = AnimeGenreSerializer(data=self.request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif self.request.method == "PUT":
            if theme_pk := kwargs.get("theme_pk"):
                query = AnimeGenreModel.objects.filter(type="anime").get(pk=theme_pk)
                instance = get_object_or_404(query, pk=theme_pk)
                serializer = AnimeGenreSerializer(
                    instance=instance, data=self.request.data, partial=True
                )
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                raise exceptions.MethodNotAllowed("`theme_pk` is required for PUT request")

    @action(
        detail=False,
        methods=["GET", "POST", "PUT"],
        filter_backends=[],
        serializer_class=AnimeGenreSerializer,
        url_path=r"genres(/(?P<genre_pk>\d+))?/?",
    )
    def anime_genres(self, *args, **kwargs):
        if self.request.method == "GET":
            query = AnimeGenreModel.objects.filter(type="anime")

            if genre_pk := kwargs.get("genre_pk"):
                query = get_object_or_404(query, pk=genre_pk)
                serializer = AnimeGenreSerializer(instance=query)
            else:
                serializer = AnimeGenreSerializer(instance=query, many=True)
            return Response(serializer.data)

        elif self.request.method == "POST":
            serializer = AnimeGenreSerializer(data=self.request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif self.request.method == "PUT":
            if genre_pk := kwargs.get("genre_pk"):
                query = AnimeGenreModel.objects.filter(type="anime")
                instance = get_object_or_404(query, pk=genre_pk)
                serializer = AnimeGenreSerializer(
                    instance=instance, data=self.request.data, partial=True
                )
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                raise exceptions.NotAcceptable("`genre_pk` is required for PUT request")

    @action(detail=True, filter_backends=[])
    def genres(self, *args, **kwargs) -> Response:
        query: AnimeModel = self.get_object()
        serializer = AnimeGenreSerializer(query.genres, many=True)
        return Response(serializer.data)

    @action(detail=True, filter_backends=[])
    def themes(self, *args, **kwargs) -> Response:
        query: AnimeModel = self.get_object()
        serializer = AnimeThemeSerializer(query.themes, many=True)
        return Response(serializer.data)

    @action(detail=True, filter_backends=[])
    def characters(self, *args, **kwargs) -> Response:
        query: AnimeModel = self.get_object()
        serializer = CharacterSerializer(query.characters, many=True)
        return Response(serializer.data)

    @action(detail=True, filter_backends=[])
    def studios(self, *args, **kwargs) -> Response:
        query: AnimeModel = self.get_object()
        serializer = ProducerSerializer(query.studios, many=True)
        return Response(serializer.data)

    @action(detail=True, filter_backends=[])
    def producers(self, *args, **kwargs) -> Response:
        query: AnimeModel = self.get_object()
        serializer = ProducerSerializer(query.producers, many=True)
        return Response(serializer.data)

    @action(detail=True, filter_backends=[])
    def staffs(self, *args, **kwargs) -> Response:
        query: AnimeModel = self.get_object()
        serializer = StaffSerializer(query.staffs, many=True)
        return Response(serializer.data)

    @action(detail=True, filter_backends=[])
    def recommendations(self, *args, **kwargs) -> Response:
        query: AnimeModel = self.get_object()
        serializer = AnimeGETSerializer(query.recommendations, many=True)
        return Response(serializer.data)

    @action(detail=True, filter_backends=[])
    def episodes(self, *args, **kwargs) -> Response:
        query: AnimeModel = self.get_object()
        serializer = EpisodeSerializer(query.episodes, many=True)
        return Response(serializer.data)
