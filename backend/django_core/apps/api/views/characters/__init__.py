from apps.api.permissions import IsSuperUserOrReadOnly
from apps.characters.models import CharacterModel
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from ...filters.character import CharacterFilter
from ...serializers.character import CharacterSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = CharacterModel.objects.all()
    serializer_class = CharacterSerializer

    # Filters
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CharacterFilter

    # Permissions
    permission_classes = (IsSuperUserOrReadOnly,)

    # Pagination
    pagination_class = LimitOffsetPagination
