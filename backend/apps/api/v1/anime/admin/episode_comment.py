from django.contrib import admin

from ..models import EpisodeCommentModel

# Register your models here.


@admin.register(EpisodeCommentModel)
class EpisodeCommentAdmin(admin.ModelAdmin):
    list_filters = ["user"]
