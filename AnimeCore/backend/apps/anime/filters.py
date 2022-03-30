from django_filters import rest_framework as filters
from .models import AnimeInfoModel
from django.db.models import Q


class AnimeInfoFilter(filters.FilterSet):
    anime = filters.CharFilter(method="anime_filter", label="Anime Name")
    genre = filters.CharFilter(method="genre_filter", label="Anime Genre")
    themes = filters.CharFilter(method="theme_filter", label="Anime Theme")
    studios = filters.CharFilter(method="studio_filter", label="Anime Studio")
    producer = filters.CharFilter(method="producer_filter", label="Anime Producer")

    class Meta:
        model = AnimeInfoModel
        fields = [
            "mal_id",
            "anime_genres__mal_id",
        ]

    def anime_filter(self, queryset, name, value):
        return queryset.filter(
            Q(anime_name_japanese__icontains=value)
            | Q(anime_name__icontains=value)
            | Q(anime_name_synonyms__name__icontains=value)
        )

    def genre_filter(self, queryset, name, value):
        """https://stackoverflow.com/questions/67343873/how-to-filter-a-comma-separated-string-in-django-rest-framework"""
        query = Q()
        for position in value.split(","):
            query |= Q(anime_genres__name__icontains=position)
        return queryset.filter(query)

    def theme_filter(self, queryset, name, value):
        """https://stackoverflow.com/questions/67343873/how-to-filter-a-comma-separated-string-in-django-rest-framework"""
        query = Q()
        for position in value.split(","):
            query |= Q(anime_themes__name__icontains=position)
        return queryset.filter(query)

    def studio_filter(self, queryset, name, value):
        """https://stackoverflow.com/questions/67343873/how-to-filter-a-comma-separated-string-in-django-rest-framework"""
        query = Q()
        for position in value.split(","):
            query |= Q(anime_studios__name__icontains=position)
        return queryset.filter(query)

    def producer_filter(self, queryset, name, value):
        """https://stackoverflow.com/questions/67343873/how-to-filter-a-comma-separated-string-in-django-rest-framework"""
        query = Q()
        for position in value.split(","):
            query |= Q(anime_producers__name__icontains=position)
        return queryset.filter(query)
