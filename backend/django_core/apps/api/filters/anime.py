from django_filters import rest_framework as filters
from apps.anime.models import AnimeModel

from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Greatest
from django.db.models.query import QuerySet


class AnimeFilter(filters.FilterSet):
    name = filters.CharFilter(method="name_filter", label="Name Filter")
    # ID's
    mal_id = filters.CharFilter(method="mal_id_filter", label="MyAnimeList ID Filter")
    kitsu_id = filters.CharFilter(method="kitsu_id_filter", label="Kitsu ID Filter")
    anilist_id = filters.CharFilter(method="anilist_id_filter", label="Anilist ID Filter")
    # many to many fields
    genre = filters.CharFilter(method="genre_filter", label="Genre Filter")
    themes = filters.CharFilter(method="themes_filter", label="Themes Filter")

    def name_filter(
        self, queryset: QuerySet[AnimeModel], name, value: str
    ) -> QuerySet[AnimeModel]:
        query = (
            queryset.annotate(
                similiarity=Greatest(
                    TrigramSimilarity("name", value),
                    TrigramSimilarity("name_japanese", value),
                    TrigramSimilarity("name_synonyms__name", value),
                )
            )
            .filter(
                similiarity__gte=0.3,
            )
            .order_by("-similiarity")
        )
        return query

    def mal_id_filter(
        self, queryset: QuerySet[AnimeModel], name: str, value: str
    ) -> QuerySet[AnimeModel]:
        query = queryset.filter(mal_id__in=value.split(","))

        return query

    def kitsu_id_filter(
        self, queryset: QuerySet[AnimeModel], name: str, value: str
    ) -> QuerySet[AnimeModel]:
        query = queryset.filter(kitsu_id__in=value.split(","))
        return query

    def anilist_id_filter(
        self, queryset: QuerySet[AnimeModel], name: str, value: str
    ) -> QuerySet[AnimeModel]:
        query = queryset.filter(anilist_id__in=value.split(","))
        return query

    def genre_filter(
        self, queryset: QuerySet[AnimeModel], name, value: str
    ) -> QuerySet[AnimeModel]:
        query = queryset.filter(genres__name__in=value.split(","))
        return query

    def theme_filter(
        self, queryset: QuerySet[AnimeModel], name: str, value: str
    ) -> QuerySet[AnimeModel]:
        query = queryset.filter(themes__name__in=value.split(","))
        return query

    def character_filter(
        self, queryset: QuerySet[AnimeModel], name: str, value: str
    ) -> QuerySet[AnimeModel]:
        query = queryset.filter(characters__name__in=value.split(","))
        return query
