from django.contrib import admin

from .models import (
    CaptureTimeStampModel,
    CaptureEpisodeModel,
    CaptureAnimeNameModel,
)

# Register your models here.

admin.site.register([CaptureTimeStampModel, CaptureEpisodeModel, CaptureAnimeNameModel])
