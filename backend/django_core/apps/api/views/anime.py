from apps.anime.models import AnimeModel
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
    AnimeThemeSerializer,
    AnimeGETSerializer,
    AnimePOSTSerializer,
)
from ..serializers.character import CharacterSerializer
from ..serializers.producer import ProducerSerializer
from ..serializers.staff import StaffSerializer
from ..serializers.episode import EpisodeSerializer


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

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "list":
            return AnimeGETSerializer
        return AnimePOSTSerializer

    @action(detail=False, filter_backends=[], url_path="themes")
    def themes_all(self, *args, **kwargs):
        query = AnimeThemeModel.objects.filter(type="anime")
        serializer = AnimeThemeSerializer(instance=query, many=True)
        return Response(serializer.data)

    @action(detail=False, filter_backends=[], url_path=r"(?P<pk>\d+)/genres")
    def genres(self, *args, **kwargs) -> Response:
        query: AnimeModel = AnimeModel.objects.get(pk=kwargs.get("pk"))
        serializer = AnimeGenreSerializer(query.genres, many=True)
        return Response(serializer.data)

    @action(detail=False, filter_backends=[], url_path=r"(?P<pk>\d+)/themes")
    def themes(self, *args, **kwargs) -> Response:
        query: AnimeModel = AnimeModel.objects.get(pk=kwargs.get("pk"))
        serializer = AnimeThemeSerializer(query.themes, many=True)
        return Response(serializer.data)

    @action(detail=False, filter_backends=[], url_path=r"(?P<pk>\d+)/characters")
    def characters(self, *args, **kwargs) -> Response:
        query: AnimeModel = AnimeModel.objects.get(pk=kwargs.get("pk"))
        serializer = CharacterSerializer(query.characters, many=True)
        return Response(serializer.data)

    @action(detail=False, filter_backends=[], url_path=r"(?P<pk>\d+)/studios")
    def studios(self, *args, **kwargs) -> Response:
        query: AnimeModel = AnimeModel.objects.get(pk=kwargs.get("pk"))
        serializer = ProducerSerializer(query.studios, many=True)
        return Response(serializer.data)

    @action(detail=False, filter_backends=[], url_path=r"(?P<pk>\d+)/producers")
    def producers(self, *args, **kwargs) -> Response:
        query: AnimeModel = AnimeModel.objects.get(pk=kwargs.get("pk"))
        serializer = ProducerSerializer(query.producers, many=True)
        return Response(serializer.data)

    @action(detail=False, filter_backends=[], url_path=r"(?P<pk>\d+)/staffs")
    def staffs(self, *args, **kwargs) -> Response:
        query: AnimeModel = AnimeModel.objects.get(pk=kwargs.get("pk"))
        serializer = StaffSerializer(query.staffs, many=True)
        return Response(serializer.data)

    @action(detail=False, filter_backends=[], url_path=r"(?P<pk>\d+)/recommendations")
    def recommendations(self, *args, **kwargs) -> Response:
        query: AnimeModel = AnimeModel.objects.get(pk=kwargs.get("pk"))
        serializer = AnimeGETSerializer(query.recommendations, many=True)
        return Response(serializer.data)

    @action(detail=False, filter_backends=[], url_path=r"(?P<pk>\d+)/episodes")
    def episodes(self, *args, **kwargs) -> Response:
        query: AnimeModel = AnimeModel.objects.get(pk=kwargs.get("pk"))
        serializer = EpisodeSerializer(query.episodes, many=True)
        return Response(serializer.data)
