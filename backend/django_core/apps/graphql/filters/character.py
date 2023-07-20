from typing import TypeVar

import strawberry_django
from apps.characters.models import CharacterModel
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Greatest

T = TypeVar("T")


@strawberry_django.filters.filter(CharacterModel)
class CharacterFilter:
    mal_id: int | None
    kitsu_id: int | None
    anilist_id: int | None

    name: str | None

    def filter_name(self, queryset: T) -> T:
        query = (
            queryset.annotate(
                similiarity=Greatest(
                    TrigramSimilarity("name", self.name),
                    TrigramSimilarity("name_kanji", self.name),
                )
            )
            .filter(
                similiarity__gte=0.3,
            )
            .order_by("-similiarity")
        )
        return query
