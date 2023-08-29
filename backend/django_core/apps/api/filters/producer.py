from apps.producers.models import ProducerModel
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Greatest
from django.db.models.query import QuerySet
from django_filters import rest_framework as filters


class ProducerFilter(filters.FilterSet):
    name = filters.CharFilter(method="name_filter", label="Name Filter")
    # ID's
    mal_id = filters.CharFilter(method="mal_id_filter", label="MyAnimeList ID Filter")
    kitsu_id = filters.CharFilter(method="kitsu_id_filter", label="Kitsu ID Filter")

    def name_filter(
        self, queryset: QuerySet[ProducerModel], name, value: str
    ) -> QuerySet[ProducerModel]:
        for _name in value.split(","):
            queryset = (
                queryset.annotate(
                    similiarity=Greatest(
                        TrigramSimilarity("name", _name),
                        TrigramSimilarity("name_japanese", _name),
                    )
                )
                .filter(
                    similiarity__gte=0.3,
                )
                .order_by("-similiarity")
            )
        return queryset

    def mal_id_filter(
        self, queryset: QuerySet[ProducerModel], name: str, value: str
    ) -> QuerySet[ProducerModel]:
        query = queryset.filter(mal_id__in=value.split(","))

        return query

    def kitsu_id_filter(
        self, queryset: QuerySet[ProducerModel], name: str, value: str
    ) -> QuerySet[ProducerModel]:
        query = queryset.filter(kitsu_id__in=value.split(","))
        return query
