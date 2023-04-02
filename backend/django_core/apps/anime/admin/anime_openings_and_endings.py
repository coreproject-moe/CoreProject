from django.contrib import admin

from ..models.anime_openings_and_endings import AnimeEndingModel, AnimeOpeningModel


@admin.register(AnimeEndingModel)
class AnimeEndingAdmin(admin.ModelAdmin[AnimeEndingModel]):
    search_fields = ["name"]


@admin.register(AnimeOpeningModel)
class AnimeOpeningAdmin(admin.ModelAdmin[AnimeOpeningModel]):
    search_fields = ["name"]
