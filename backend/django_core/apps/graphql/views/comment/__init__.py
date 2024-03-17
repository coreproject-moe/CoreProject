from apps.comments.models import CommentModel
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import mixins

from ...filters.comments import CommentFilter
from ...serializers.comments import CommentSerializer

from django.db.models import Count


class CommentViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

    # Filters
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CommentFilter

    # Permissions
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # Pagination
    pagination_class = LimitOffsetPagination

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def perform_destroy(self, instance: CommentModel) -> None:
        if instance.childrens == 0:
            instance.delete()

        else:
            instance.deleted = True
            instance.text = ""
            instance.user = None
            instance.save()

        for item in CommentModel.objects.filter(deleted=True):
            if item.childrens == 0:
                item.delete()
