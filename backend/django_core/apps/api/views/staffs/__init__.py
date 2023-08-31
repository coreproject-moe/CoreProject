from apps.api.permissions import IsSuperUserOrReadOnly
from apps.staffs.models import StaffModel
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from ...filters.staff import StaffFilter
from ...serializers.staffs import StaffSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = StaffModel.objects.all()
    serializer_class = StaffSerializer

    # Filters
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StaffFilter

    # Permissions
    permission_classes = (IsSuperUserOrReadOnly,)

    # Pagination
    pagination_class = LimitOffsetPagination
