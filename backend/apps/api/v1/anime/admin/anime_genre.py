from django.contrib import admin
from core.admin import site
from ..models import AnimeGenreModel

# Register your models here.


class AnimeGenreAdmin(admin.ModelAdmin):
    search_fields = ["name"]


site.register(AnimeGenreModel, AnimeGenreAdmin)
