from django.contrib import admin

from ..forms import EpisodeAdminModelForm
from ..models import EpisodeModel

# Register your models here.


@admin.register(EpisodeModel)
class EpisodeAdmin(admin.ModelAdmin[EpisodeModel]):
    form = EpisodeAdminModelForm
    search_fields = ["episode_name"]


from .episode_timestamp import EpisodeTimestampAdmin as EpisodeTimestampAdmin
