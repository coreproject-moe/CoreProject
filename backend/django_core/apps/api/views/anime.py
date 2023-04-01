from apps.anime.models import AnimeModel
from apps.anime.models.anime_genre import AnimeGenreModel
from apps.anime.models.anime_theme import AnimeThemeModel
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
    AnimeGETSerializer,
    AnimePOSTSerializer,
    AnimeThemeSerializer,
)
from ..serializers.character import CharacterSerializer
from ..serializers.episode import EpisodeSerializer
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
    serializer_class = AnimePOSTSerializer
    queryset = AnimeModel.objects.all()
    lookup_field = "pk"
    # Capture only integers
    lookup_value_regex = "\d+"

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "list":
            return AnimeGETSerializer
        return AnimePOSTSerializer

    @action(detail=False, methods=["GET", "POST"], filter_backends=[], url_path="themes")
    def anime_themes(self, *args, **kwargs):
        query = AnimeThemeModel.objects.filter(type="anime")
        serializer = AnimeThemeSerializer(instance=query, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["GET", "POST"], filter_backends=[], url_path="themes")
    def anime_genres(self, *args, **kwargs):
        query = AnimeGenreModel.objects.filter(type="anime")
        serializer = AnimeGenreSerializer(instance=query, many=True)
        return Response(serializer.data)

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
