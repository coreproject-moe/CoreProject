from django.contrib import admin

from .models import (
    AnimeInfoModel,
    EpisodeModel,
    EpisodeCommentModel,
    EpisodeTimestampModel,
    AnimeGenreModel,
    AnimeThemeModel,
    AnimeStudioModel,
    AnimeProducerModel,
    AnimeSynonymModel,
    AnimeRecommendationModel,
)

# Register your models here.


@admin.register(AnimeRecommendationModel)
class AnimeRecommendationAdmin(admin.ModelAdmin):
    raw_id_fields = ("entry",)


@admin.register(AnimeInfoModel)
class AnimeInfoAdmin(admin.ModelAdmin):
    filter_horizontal = [
        "anime_genres",
        "anime_themes",
        "anime_studios",
        "anime_producers",
        "anime_name_synonyms",
        "anime_episodes",
    ]


@admin.register(AnimeGenreModel)
class AnimeGenreAdmin(admin.ModelAdmin):
    """"""

    # https://stackoverflow.com/questions/49293901/hide-model-from-main-admin-list-but-allow-creation-in-inline-editor
    # def has_module_permission(self, request):
    #     return False


admin.site.register(
    [
        EpisodeModel,
        EpisodeCommentModel,
        EpisodeTimestampModel,
        AnimeThemeModel,
        AnimeStudioModel,
        AnimeProducerModel,
        AnimeSynonymModel,
    ]
)
