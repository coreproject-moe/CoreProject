from django.contrib import admin

from ..models import EpisodeModel

# Register your models here.


@admin.register(EpisodeModel)
class EpisodeAdmin(admin.ModelAdmin[EpisodeModel]):
    search_fields = ["episode_name"]


from .episode_comment import EpisodeCommentAdmin as EpisodeCommentAdmin
from .episode_timestamp import EpisodeTimestampAdmin as EpisodeTimestampAdmin
