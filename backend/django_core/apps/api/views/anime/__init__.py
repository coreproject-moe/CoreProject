from apps.anime.models import AnimeModel, AnimeCommentModel
from apps.api.permissions import IsSuperUserOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ...filters.anime import AnimeFilter
from ...serializers.anime import AnimeGETSerializer, AnimePOSTSerializer
from ...serializers.anime.comment import AnimeCommentSerializer

from django.http import HttpRequest
from rest_framework.response import Response


class AnimeViewSet(viewsets.ModelViewSet):
    queryset = AnimeModel.objects.all()

    # Filters
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AnimeFilter

    # Permissions
    permission_classes = (IsSuperUserOrReadOnly,)

    # Pagination
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self) -> type[AnimeGETSerializer] | type[AnimePOSTSerializer]:
        if self.request.method == "GET":
            return AnimeGETSerializer
        else:
            return AnimePOSTSerializer
