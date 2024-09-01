from typing import TypeVar

from apps.comments.models import CommentModel
import strawberry_django

T = TypeVar("T")


@strawberry_django.filters.filter(CommentModel)
class CommentFilter:
    path: str

    def filter_path(self, queryset: T) -> T:
        query = queryset.filter(path__descendants=self.path)
        return query
