from django.contrib import admin

from .models import AnimeNameModel, EpisodeModel

# Register your models here.

admin.site.register(EpisodeModel)
admin.site.register(AnimeNameModel)
