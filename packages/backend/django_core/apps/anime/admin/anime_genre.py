from django.contrib import admin

from ..models.anime_genre import AnimeGenreModel

# Register your models here.


@admin.register(AnimeGenreModel)
class AnimeGenreAdmin(admin.ModelAdmin[AnimeGenreModel]):
    search_fields = ["name"]
