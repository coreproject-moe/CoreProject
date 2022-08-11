from django.contrib import admin
from core.admin import site
from ..models import EpisodeModel

# Register your models here.


class EpisodeAdmin(admin.ModelAdmin):
    search_fields = ["episode_name"]


site.register(EpisodeModel, EpisodeAdmin)
