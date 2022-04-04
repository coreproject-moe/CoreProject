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
class AnimeRecommendationAdmin(admin.ModelAdmin):
    raw_id_fields = ("entry",)


admin.site.register(AnimeRecommendationModel, AnimeRecommendationAdmin)

admin.site.register(
    [
        AnimeInfoModel,
        EpisodeModel,
        EpisodeCommentModel,
        EpisodeTimestampModel,
        AnimeGenreModel,
        AnimeThemeModel,
        AnimeStudioModel,
        AnimeProducerModel,
        AnimeSynonymModel,
    ]
)
