from django.contrib import admin

from ..models import AnimeInfoModel

# Register your models here.


@admin.register(AnimeInfoModel)
class AnimeInfoAdmin(admin.ModelAdmin):
    autocomplete_fields = []

    filter_horizontal = [
        "anime_genres",
        "anime_themes",
        "anime_studios",
        "anime_episodes",
        "anime_producers",
        "anime_name_synonyms",
        "anime_recommendation",
    ]

    list_filter = [
        "anime_genres",
        "anime_themes",
        "anime_studios",
        "anime_producers",
    ]

    search_fields = [
        "anime_name",
    ]
