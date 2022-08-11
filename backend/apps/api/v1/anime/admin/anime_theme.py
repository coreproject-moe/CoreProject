from django.contrib import admin
from core.admin import site
from ..models import AnimeThemeModel

# Register your models here.


class AnimeThemeAdmin(admin.ModelAdmin):
    search_fields = ["name"]


site.register(AnimeThemeModel, AnimeThemeAdmin)
