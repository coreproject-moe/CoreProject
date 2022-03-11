from django.contrib import admin

from .models import CaptureVideoModel, CaptureEpisodeModel, CaptureAnimeNameModel

# Register your models here.

admin.site.register(CaptureVideoModel)
admin.site.register(CaptureEpisodeModel)
admin.site.register(CaptureAnimeNameModel)
