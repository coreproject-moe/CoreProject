import strawberry_django
from apps.comments.models import CommentModel
from typing import TypeVar
from strawberry import Info
from strawberry_django.filters import _QS
from django.db.models import Q


T = TypeVar("T")


@strawberry_django.filters.filter(CommentModel)
class CommentFilter:
    path: str

    def filter_path(self, queryset: T) -> T:
        query = queryset.filter(path__descendants=self.path)
        return query
