from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from django.contrib import admin
from django import forms

from ..models import AnimeModel
from django_admin_hstore_widget.forms import HStoreFormField


# Register your models here.


class AnimeAdminModelForm(forms.ModelForm):
    anime_theme_openings = HStoreFormField()
    anime_theme_endings = HStoreFormField()

    class Meta:
        model = AnimeModel
        exclude = ()


@admin.register(AnimeModel)
class AnimeInfoAdmin(admin.ModelAdmin, DynamicArrayMixin):
    form = AnimeAdminModelForm
    formfield_overrides = {"hello": {"widgets": HStoreFormField}}
    filter_horizontal = [
        "anime_genres",
        "anime_themes",
        "anime_studios",
        "anime_producers",
        "anime_characters",
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
        (
            None,
            {
                "fields": (
                    "anime_theme_openings",
                    "anime_theme_endings",
                ),
            },
        ),
    )


# https://stackoverflow.com/questions/49293901/hide-model-from-main-admin-list-but-allow-creation-in-inline-editor
# def has_module_permission(self:Self, request):
#     return False


from .anime_genre import AnimeGenreAdmin as AnimeGenreAdmin
from .anime_theme import AnimeThemeAdmin as AnimeThemeAdmin
