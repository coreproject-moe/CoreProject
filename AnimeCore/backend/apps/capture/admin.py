from django.contrib import admin

from .models import (
    CaptureInfoModel,
    CaptureEpisodeModel,
    CaptureAnimeNameModel,
)

# Register your models here.

admin.site.register(CaptureInfoModel)
admin.site.register(CaptureEpisodeModel)
admin.site.register(CaptureAnimeNameModel)
