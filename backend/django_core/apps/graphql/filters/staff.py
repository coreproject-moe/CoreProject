from typing import TypeVar

import strawberry_django
from apps.staffs.models import StaffModel
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Greatest
from strawberry import auto

T = TypeVar("T")


@strawberry_django.filters.filter(StaffModel)
class StaffFilter:
    mal_id: int | None
    kitsu_id: int | None
    anilist_id: int | None

    name: str | None

    def filter_name(self, queryset: T) -> T:
        query = (
            queryset.annotate(
                similiarity=Greatest(
                    TrigramSimilarity("name", self.name),
                    TrigramSimilarity("alternate_names__name", self.name),
                    TrigramSimilarity("family_name", self.name),
                    TrigramSimilarity("given_name", self.name),
                )
            )
            .filter(
                similiarity__gte=0.3,
            )
            .order_by("-similiarity")
        )
        return query
