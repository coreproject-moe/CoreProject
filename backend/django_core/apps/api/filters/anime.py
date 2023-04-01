from apps.anime.models import AnimeModel
from django_filters import rest_framework as filters

from django.db.models import Q


class AnimeFilter(filters.FilterSet):
    name = filters.CharFilter(method="anime_name_filter", label="Anime Name")

    class Meta:
        model = AnimeModel
        fields = [
            "mal_id",
        ]

    def anime_name_filter(self, queryset, name, value):
        return queryset.filter(
            Q(name_japanese__icontains=value)
            | Q(name__icontains=value)
            | Q(name_synonyms__name__icontains=value)
        )
