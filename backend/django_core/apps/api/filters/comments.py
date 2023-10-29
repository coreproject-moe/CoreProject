from apps.episodes.models.episode_comment import EpisodeCommentModel
from django.db.models.query import QuerySet
from django_filters import rest_framework as filters


class EpisodeCommentFilter(filters.FilterSet):
    path = filters.CharFilter(method="path_filter", label="Path Filter")

    def path_filter(
        self, queryset: QuerySet[EpisodeCommentModel], name: str, value: str
    ) -> QuerySet[EpisodeCommentModel]:
        queryset = queryset.filter(path__descendants=value)
        print(queryset.query)
        return queryset
