from django.contrib import admin

from ..forms import AnimeAdminModelForm
from ..models import AnimeModel, AnimeNameSynonymModel


# Register your models here.
@admin.register(AnimeNameSynonymModel)
class AnimeNameSynonymAdmin(
    admin.ModelAdmin[AnimeNameSynonymModel],
):
    pass


@admin.register(AnimeModel)
class AnimeInfoAdmin(admin.ModelAdmin[AnimeModel]):
    form = AnimeAdminModelForm
    filter_horizontal = [
        "genres",
        "themes",
        "studios",
        "producers",
        "characters",
        "name_synonyms",
        "recommendations",
        "episodes",
    ]
    list_filter = [
        "genres",
        "themes",
        "studios",
        "producers",
        "characters",
    ]
    search_fields = [
        "name",
    ]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "mal_id",
                    "kitsu_id",
                    "anilist_id",
                ),
            },
        ),
        (
            ("Anime Names"),
            {
                "fields": (
                    "name",
                    "name_japanese",
                ),
            },
        ),
        (
            ("Image Colors"),
            {
                "fields": (
                    "banner_background_color",
                    "cover_background_color",
                ),
            },
        ),
        (
            ("Anime Rating"),
            {
                "fields": ("rating",),
            },
        ),
        (
            ("Anime Time Info"),
            {
                "fields": (
                    "aired_from",
                    "aired_to",
                )
            },
        ),
        (
            ("Anime Images"),
            {
                "fields": (
                    "cover",
                    "banner",
                )
            },
        ),
        (
            ("Anime Background & Summary"),
            {
                "fields": (
                    "synopsis",
                    "background",
                )
            },
        ),
        (
            ("Anime M2M Fields"),
            {
                "fields": (
                    "genres",
                    "themes",
                    "studios",
                    "producers",
                    "characters",
                    "name_synonyms",
                    "recommendations",
                )
            },
        ),
        (
            ("Anime Episodes"),
            {
                "fields": ("episodes",),
            },
        ),
        (
            None,
            {
                "fields": (
                    "theme_openings",
                    "theme_endings",
                ),
            },
        ),
    )


# https://stackoverflow.com/questions/49293901/hide-model-from-main-admin-list-but-allow-creation-in-inline-editor
# def has_module_permission(self:Self, request):
#     return False


from .anime_genre import AnimeGenreAdmin as AnimeGenreAdmin
from .anime_theme import AnimeThemeAdmin as AnimeThemeAdmin
