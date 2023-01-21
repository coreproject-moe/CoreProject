from django.contrib import admin

from ..models import AnimeThemeModel

# Register your models here.


@admin.register(AnimeThemeModel)
class AnimeThemeAdmin(admin.ModelAdmin[AnimeThemeModel]):
    search_fields = ["name"]
