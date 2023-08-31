from apps.anime.models import AnimeModel
from apps.api.permissions import IsSuperUserOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from ...filters.anime import AnimeFilter
from ...serializers.anime import AnimeGETSerializer, AnimePOSTSerializer


class AnimeViewSet(
    viewsets.ModelViewSet,
):
    queryset = AnimeModel.objects.all()

    # Filters
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AnimeFilter

    # Permissions
    permission_classes = (IsSuperUserOrReadOnly,)

    # Pagination
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        if self.request.method == "GET":
            return AnimeGETSerializer
        else:
            return AnimePOSTSerializer
