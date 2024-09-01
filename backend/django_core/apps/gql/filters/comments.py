import strawberry_django
from apps.comments.models import CommentModel
from typing import TypeVar


T = TypeVar("T")


@strawberry_django.filters.filter(CommentModel)
class CommentFilter:
    path: str

    def filter_path(self, queryset: T) -> T:
        query = queryset.filter(path__descendants=self.path)
        return query
