from rest_framework import viewsets
from apps.comments.models import CommentModel
from django_filters.rest_framework import DjangoFilterBackend

from ...serializers.comments import CommentSerializer
from ...filters.comments import CommentFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CommentViewSet(viewsets.ModelViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

    # Filters
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CommentFilter

    # Permissions
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # Pagination
    pagination_class = LimitOffsetPagination
