from apps.comments.models import CommentModel
from django.contrib.postgres.fields import HStoreField
from django.db import models
from dynamic_filenames import FilePattern
from mixins.models.created_at import CreatedAtMixin
from mixins.models.updated_at import UpdatedAtMixin

from .episode_timestamp import EpisodeTimestampModel

episode_pattern = FilePattern(filename_pattern="episode/{uuid:s}{ext}")
episode_thumbnail_pattern = FilePattern(filename_pattern="thumbnail/{uuid:s}{ext}")

# Create your models here.
EPISODE_TYPE = [
    ("sub", "sub"),
    ("dub", "dub"),
]


class EpisodeModel(UpdatedAtMixin, CreatedAtMixin):
    episode_number = models.BigIntegerField(default=0)
    episode_name = models.CharField(max_length=1024)
    episode_thumbnail = models.ImageField(
        upload_to=episode_thumbnail_pattern,
        default=None,
        blank=True,
        null=True,
    )

    episode_summary = models.TextField(default="", blank=True, null=True)

    episode_comments = models.ManyToManyField(CommentModel, blank=True)
    episode_timestamps = models.ManyToManyField(EpisodeTimestampModel, blank=True)

    episode_length = models.PositiveIntegerField(
        default=None,
        blank=True,
    )
    # Sub or Dub
    episode_type = models.CharField(
        max_length=3,
        choices=EPISODE_TYPE,
        blank=True,
    )
    # Extra providers
    providers = HStoreField(
        default=dict,
        null=False,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.episode_number}. {self.episode_name}"

    class Meta:
        verbose_name = "Episode"
        verbose_name_plural = "Episodes"


from .episode_timestamp import EpisodeTimestampModel as EpisodeTimestampModel
