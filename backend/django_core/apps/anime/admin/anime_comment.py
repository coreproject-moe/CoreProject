from django.contrib import admin

from ..models import AnimeCommentModel


@admin.register(AnimeCommentModel)
class AnimeCommentAdmin(admin.ModelAdmin[AnimeCommentModel]):
    search_fields = ["name"]
