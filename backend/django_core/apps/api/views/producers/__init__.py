from apps.api.permissions import IsSuperUserOrReadOnly
from apps.producers.models import ProducerModel
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from ...filters.producer import ProducerFilter
from ...serializers.producers import ProducerSerializer


class ProducerViewSet(viewsets.ModelViewSet):
    queryset = ProducerModel.objects.all()
    serializer_class = ProducerSerializer

    # Filters
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProducerFilter

    # Permissions
    permission_classes = (IsSuperUserOrReadOnly,)

    # Pagination
    pagination_class = LimitOffsetPagination
