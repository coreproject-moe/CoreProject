from django.contrib import admin

from ..models import EpisodeModel

# Register your models here.


@admin.register(EpisodeModel)
class EpisodeAdmin(admin.ModelAdmin):
    search_fields = ["episode_name"]
