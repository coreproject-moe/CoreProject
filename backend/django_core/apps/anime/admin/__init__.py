from django.contrib import admin

from ..forms import AnimeAdminModelForm
from ..models import AnimeModel, AnimeNameSynonymModel


# Register your models here.
@admin.register(AnimeNameSynonymModel)
class AnimeNameSynonymAdmin(
    admin.ModelAdmin[AnimeNameSynonymModel],
):
    search_fields = ["name"]
    pass


@admin.register(AnimeModel)
class AnimeInfoAdmin(admin.ModelAdmin[AnimeModel]):
    form = AnimeAdminModelForm
    autocomplete_fields = [
        "genres",
        "themes",
        "studios",
        "producers",
        "staffs",
        "characters",
        "name_synonyms",
        "recommendations",
        "episodes",
        "openings",
        "endings",
    ]
    list_filter = [
        "genres",
        "themes",
        # "studios",
        # "producers",
        # "characters",
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
            ("Anime Source"),
            {
                "fields": ("source",),
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
                    "staffs",
                    "characters",
                    "name_synonyms",
                    "recommendations",
                    "openings",
                    "endings",
                    "comments",
                )
            },
        ),
        (
            ("Anime Episodes"),
            {
                "fields": ("episodes",),
            },
        ),
    )


# https://stackoverflow.com/questions/49293901/hide-model-from-main-admin-list-but-allow-creation-in-inline-editor
# def has_module_permission(self:Self, request):
#     return False


from .anime_comment import AnimeCommentAdmin as AnimeCommentAdmin
from .anime_genre import AnimeGenreAdmin as AnimeGenreAdmin
from .anime_openings_and_endings import (
    AnimeEndingAdmin as AnimeEndingAdmin,
)
from .anime_openings_and_endings import (
    AnimeOpeningAdmin as AnimeOpeningAdmin,
)
from .anime_theme import AnimeThemeAdmin as AnimeThemeAdmin
