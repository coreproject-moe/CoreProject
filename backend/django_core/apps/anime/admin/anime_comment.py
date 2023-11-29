from ..models import AnimeCommentModel
from django.contrib import admin


@admin.register(AnimeCommentModel)
class AnimeCommentAdmin(admin.ModelAdmin[AnimeCommentModel]):
    search_fields = ["name"]
