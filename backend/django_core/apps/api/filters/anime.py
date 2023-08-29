from apps.anime.models import AnimeModel
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import Q
from django.db.models.functions import Greatest
from django.db.models.query import QuerySet
from django_filters import rest_framework as filters


class AnimeFilter(filters.FilterSet):
    name = filters.CharFilter(method="name_filter", label="Name Filter")
    # ID's
    mal_id = filters.CharFilter(method="mal_id_filter", label="MyAnimeList ID Filter")
    kitsu_id = filters.CharFilter(method="kitsu_id_filter", label="Kitsu ID Filter")
    anilist_id = filters.CharFilter(method="anilist_id_filter", label="Anilist ID Filter")
    # many to many fields
    genre = filters.CharFilter(method="genre_filter", label="Genre Filter")
    themes = filters.CharFilter(method="themes_filter", label="Theme Filter")
    characters = filters.CharFilter(method="character_filter", label="Character Filter")
    studios = filters.CharFilter(method="studio_filter", label="Studio Filter")
    producers = filters.CharFilter(method="producer_filter", label="Producer Filter")
    staffs = filters.CharFilter(method="staff_filter", label="Staff Filter")

    def name_filter(
        self, queryset: QuerySet[AnimeModel], name, value: str
    ) -> QuerySet[AnimeModel]:
        for _name in value.split(","):
            queryset = (
                queryset.annotate(
                    similiarity=Greatest(
                        TrigramSimilarity("name", _name),
                        TrigramSimilarity("name_japanese", _name),
                        TrigramSimilarity("name_synonyms__name", _name),
                    )
                )
                .filter(
                    similiarity__gte=0.3,
                )
                .order_by("-similiarity")
            )
        return queryset

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
        for _name in value.split(","):
            queryset = (
                queryset.annotate(
                    similiarity=Greatest(
                        TrigramSimilarity("characters__name", _name),
                        TrigramSimilarity("characters__name_kanji", _name),
                    )
                )
                .filter(
                    similiarity__gte=0.3,
                )
                .order_by("-similiarity")
            )
        return queryset

    def studio_filter(
        self, queryset: QuerySet[AnimeModel], name: str, value: str
    ) -> QuerySet[AnimeModel]:
        query = queryset.filter(studios__name__in=value.split(","))
        return query

    def producer_filter(
        self, queryset: QuerySet[AnimeModel], name: str, value: str
    ) -> QuerySet[AnimeModel]:
        query = queryset.filter(producers__name__in=value.split(","))
        return query

    def staff_filter(
        self, queryset: QuerySet[AnimeModel], name: str, value: str
    ) -> QuerySet[AnimeModel]:
        for _name in value.split(","):
            queryset = (
                queryset.annotate(
                    similarity=Greatest(
                        TrigramSimilarity("staffs__name", _name),
                        TrigramSimilarity("staffs__given_name", _name),
                        TrigramSimilarity("staffs__family_name", _name),
                        TrigramSimilarity("staffs__alternate_names__name", _name),
                    )
                )
                .filter(Q(similarity__gte=0.3))
                .order_by("-similarity")
            )

        return queryset
