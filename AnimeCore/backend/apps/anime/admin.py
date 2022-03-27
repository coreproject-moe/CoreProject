from django.contrib import admin

from .models import (
    AnimeInfoModel,
    EpisodeModel,
    EpisodeCommentModel,
    EpisodeTimestampModel,
    AnimeGenreModel,
)

# Register your models here.


admin.site.register(
    [
        AnimeInfoModel,
        EpisodeModel,
        EpisodeCommentModel,
        EpisodeTimestampModel,
        AnimeGenreModel,
    ]
)
