from apps.api.permissions import IsSuperUserOrReadOnly
from apps.staffs.models import StaffModel
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, viewsets

from ...filters.staff import StaffFilter
from ...serializers.staffs import StaffSerializer


class StaffViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = StaffModel.objects.all()
    serializer_class = StaffSerializer

    # Filters
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StaffFilter

    # Permissions
    permission_classes = (IsSuperUserOrReadOnly,)


class StaffSpecificAPIView(
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset = StaffModel.objects.all()
    serializer_class = StaffSerializer
    permission_classes = (IsSuperUserOrReadOnly,)
