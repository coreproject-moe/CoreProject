from django_filters import rest_framework as filters
from apps.anime.models import AnimeModel

from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Greatest


class AnimeFilter(filters.FilterSet):
    name = filters.CharFilter(method="name_filter", label="Name Filter")
    mal_id = filters.CharFilter(method="mal_id_filter", label="MyAnimeList ID Filter")
    kitsu_id = filters.CharFilter(method="kitsu_id_filter", label="Kitsu ID Filter")

    def mal_id_filter(self, queryset: AnimeModel, name, value: str) -> AnimeModel:
        query = queryset.filter(mal_id__in=list(map(int, value.split(","))))
        return query

    def kitsu_id_filter(self, queryset: AnimeModel, name, value: str) -> AnimeModel:
        query = queryset.filter(kitsu_id__in=list(map(int, value.split(","))))
        return query

    def name_filter(self, queryset: AnimeModel, name, value: str) -> AnimeModel:
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
        print(query.query)
        return query
