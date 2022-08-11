from django.contrib import admin
from ..models import AnimeModel

# Register your models here.


@admin.register(AnimeModel)
class AnimeInfoAdmin(admin.ModelAdmin):
    filter_horizontal = [
        "anime_genres",
        "anime_themes",
        "anime_studios",
        "anime_producers",
        "anime_characters",
        "anime_name_synonyms",
        "anime_recommendation",
        "anime_episodes",
    ]

    list_filter = [
        "anime_genres",
        "anime_themes",
        "anime_studios",
        "anime_producers",
        "anime_characters",
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
                    "anime_characters",
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

    def get_app_list():
        x = super().get_app_list()

        print(x)
        return x


# https://stackoverflow.com/questions/49293901/hide-model-from-main-admin-list-but-allow-creation-in-inline-editor
# def has_module_permission(self, request):
#     return False


# Extra Imports
# __ DO NOT REMOVE __

from .anime_theme import AnimeThemeAdmin
from .anime_genre import AnimeGenreAdmin
from .anime_synonym import AnimeSynonymAdmin
from .episode import EpisodeAdmin
from .episode_comment import EpisodeCommentAdmin
from .episode_timestamp import EpisodeTimestampAdmin
