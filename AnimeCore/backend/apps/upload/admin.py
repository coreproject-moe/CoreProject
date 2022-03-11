from django.contrib import admin

from .models import AnimeInfoModel, EpisodeModel

# Register your models here.

admin.site.register(EpisodeModel)
admin.site.register(AnimeInfoModel)
