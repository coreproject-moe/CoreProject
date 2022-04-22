from django.contrib import admin

from ..models import AnimeRecommendationModel

# Register your models here.


@admin.register(AnimeRecommendationModel)
class AnimeRecommendationAdmin(admin.ModelAdmin):
    search_fields = ["entry__anime_name"]
    autocomplete_fields = ["entry", "anime"]
