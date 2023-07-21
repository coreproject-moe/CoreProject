from typing import TypeVar

import strawberry
from apps.anime.models import AnimeModel
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Greatest

from .anime_genre import AnimeGenreFilter
from .anime_theme import AnimeThemeFilter
from .character import CharacterFilter
from .producer import ProducerFilter
from .staff import StaffFilter

T = TypeVar("T")


@strawberry.django.filters.filter(AnimeModel)
class AnimeFilter:
    id: int | None

    # ID based lookups
    mal_id: int | None
    kitsu_id: int | None
    anilist_id: int | None

    name: str | None

    def filter_name(self, queryset: T) -> T:
        query = (
            queryset.annotate(
                similiarity=Greatest(
                    TrigramSimilarity("name", self.name),
                    TrigramSimilarity("name_japanese", self.name),
                    TrigramSimilarity("name_synonyms__name", self.name),
                )
            )
            .filter(
                similiarity__gte=0.3,
            )
            .order_by("-similiarity")
        )

        return query

    genres: AnimeGenreFilter | None
    themes: AnimeThemeFilter | None

    staffs: StaffFilter | None
    characters: CharacterFilter | None

    # Studios and producer share same model
    studios: ProducerFilter | None
    producers: ProducerFilter | None
    