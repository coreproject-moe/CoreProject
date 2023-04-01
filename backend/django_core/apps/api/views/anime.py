from apps.anime.models import AnimeModel
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response

from ..filters.anime import AnimeFilter
from ..serializers.anime import (
    AnimeGenreSerializer,
    AnimeSerializer,
    AnimeThemeSerializer,
)
from ..serializers.character import CharacterSerializer
from ..serializers.producer import ProducerSerializer
from ..serializers.staff import StaffSerializer


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
    serializer_class = AnimeSerializer
    queryset = AnimeModel.objects.all()
    lookup_field = "pk"

    @action(detail=True, methods=["GET"], filter_backends=[])
    def genres(self, *args, **kwargs) -> Response:
        query: AnimeModel = self.get_object()
        serializer = AnimeGenreSerializer(query.genres, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"], filter_backends=[])
    def themes(self, *args, **kwargs) -> Response:
        query: AnimeModel = self.get_object()
        serializer = AnimeThemeSerializer(query.themes, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"], filter_backends=[])
    def characters(self, *args, **kwargs) -> Response:
        query: AnimeModel = self.get_object()
        serializer = CharacterSerializer(query.characters, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"], filter_backends=[])
    def studios(self, *args, **kwargs) -> Response:
        query: AnimeModel = self.get_object()
        serializer = ProducerSerializer(query.studios, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"], filter_backends=[])
    def producers(self, *args, **kwargs) -> Response:
        query: AnimeModel = self.get_object()
        serializer = ProducerSerializer(query.producers, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"], filter_backends=[])
    def staffs(self, *args, **kwargs) -> Response:
        query: AnimeModel = self.get_object()
        serializer = StaffSerializer(query.staffs, many=True)
        return Response(serializer.data)
