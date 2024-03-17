from apps.comments.models import CommentModel
from django.db.models.query import QuerySet
from django_filters import rest_framework as filters


class CommentFilter(filters.FilterSet):
    path = filters.CharFilter(method="path_filter", label="Path Filter")

    def path_filter(
        self, queryset: QuerySet[CommentModel], name: str, value: str
    ) -> QuerySet[CommentModel]:
        queryset = queryset.filter(path__descendants=value)
        return queryset
