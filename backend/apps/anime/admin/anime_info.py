from django.contrib import admin

from ..models import AnimeInfoModel

# Register your models here.


@admin.register(AnimeInfoModel)
class AnimeInfoAdmin(admin.ModelAdmin):
    filter_horizontal = [
        "anime_genres",
        "anime_themes",
        "anime_studios",
        "anime_producers",
        "anime_name_synonyms",
        "anime_recommendation",
        "anime_episodes",
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

    fieldsets = (
        (
            None,
            {
                "fields": ("mal_id",),
            },
        ),
        (
            ("Anime Names"),
            {
                "fields": (
                    "anime_name",
                    "anime_name_japanese",
                ),
            },
        ),
        (
            ("Anime Rating"),
            {
                "fields": ("anime_rating",),
            },
        ),
        (
            ("Anime Time Info"),
            {
                "fields": (
                    "anime_aired_from",
                    "anime_aired_to",
                )
            },
        ),
        (
            ("Anime Images"),
            {
                "fields": (
                    "anime_cover",
                    "anime_banner",
                )
            },
        ),
        (
            ("Anime Background & Summary"),
            {
                "fields": (
                    "anime_synopsis",
                    "anime_background",
                )
            },
        ),
        (
            ("Anime M2M Fields"),
            {
                "fields": (
                    "anime_genres",
                    "anime_themes",
                    "anime_studios",
                    "anime_producers",
                    "anime_name_synonyms",
                    "anime_recommendation",
                )
            },
        ),
        (
            ("Anime Episodes"),
            {
                "fields": ("anime_episodes",),
            },
        ),
    )
