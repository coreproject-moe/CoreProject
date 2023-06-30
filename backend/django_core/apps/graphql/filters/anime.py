import strawberry
from apps.anime.models import AnimeModel
from django.db.models.functions import Greatest
from django.contrib.postgres.search import TrigramSimilarity
from typing import TypeVar

from .staff import StaffFilter

from .producer import ProducerFilter
from .anime_genre import AnimeGenreFilter
from .anime_theme import AnimeThemeFilter

QUERYSET = TypeVar("QUERYSET")


@strawberry.django.filters.filter(AnimeModel)
class AnimeFilter:
    id: int

    # ID based lookups
    mal_id: int
    kitsu_id: int
    anilist_id: int

    name: str

    def filter_name(self, queryset: QUERYSET) -> QUERYSET:
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

        print(query.query)
        return query

    genres: AnimeGenreFilter
    themes: AnimeThemeFilter

    # Studios and producer share same model
    studios: ProducerFilter
    producers: ProducerFilter

    staffs: StaffFilter
