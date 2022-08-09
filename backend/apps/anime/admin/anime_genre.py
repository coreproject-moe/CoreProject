from django.contrib import admin

from ..models import AnimeGenreModel

# Register your models here.


@admin.register(AnimeGenreModel)
class AnimeGenreAdmin(admin.ModelAdmin):
    search_fields = ["name"]
