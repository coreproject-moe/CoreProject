from apps.characters.models import CharacterModel
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Greatest
from django.db.models.query import QuerySet
from django_filters import rest_framework as filters


class CharacterFilter(filters.FilterSet):
    name = filters.CharFilter(method="name_filter", label="Name Filter")
    # ID's
    mal_id = filters.CharFilter(method="mal_id_filter", label="MyAnimeList ID Filter")
    kitsu_id = filters.CharFilter(method="kitsu_id_filter", label="Kitsu ID Filter")
    anilist_id = filters.CharFilter(method="anilist_id_filter", label="Anilist ID Filter")

    def name_filter(
        self, queryset: QuerySet[CharacterModel], name, value: str
    ) -> QuerySet[CharacterModel]:
        for _name in value.split(","):
            queryset = (
                queryset.annotate(
                    similiarity=Greatest(
                        TrigramSimilarity("name", _name),
                        TrigramSimilarity("name_kanji", _name),
                    )
                )
                .filter(
                    similiarity__gte=0.3,
                )
                .order_by("-similiarity")
            )
        return queryset

    def mal_id_filter(
        self, queryset: QuerySet[CharacterModel], name: str, value: str
    ) -> QuerySet[CharacterModel]:
        query = queryset.filter(mal_id__in=value.split(","))

        return query

    def kitsu_id_filter(
        self, queryset: QuerySet[CharacterModel], name: str, value: str
    ) -> QuerySet[CharacterModel]:
        query = queryset.filter(kitsu_id__in=value.split(","))
        return query

    def anilist_id_filter(
        self, queryset: QuerySet[CharacterModel], name: str, value: str
    ) -> QuerySet[CharacterModel]:
        query = queryset.filter(anilist_id__in=value.split(","))
        return query
