from apps.producers.models import ProducerModel
from apps.api.permissions import IsSuperUserOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, viewsets

from ...filters.producer import ProducerFilter
from ...serializers.producers import ProducerSerializer


class ProducerViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = ProducerModel.objects.all()
    serializer_class = ProducerSerializer

    # Filters
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProducerFilter

    # Permissions
    permission_classes = (IsSuperUserOrReadOnly,)


class ProducerSpecificAPIView(
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset = ProducerModel.objects.all()
    serializer_class = ProducerSerializer
    permission_classes = (IsSuperUserOrReadOnly,)
