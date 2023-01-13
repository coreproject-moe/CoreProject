from core.storages import OverwriteStorage
from django.db import models
from dynamic_filenames import FilePattern

from .episode_comment import EpisodeCommentModel
from .episode_timestamp import EpisodeTimestampModel

episode_cover = FilePattern(filename_pattern="/episode_cover{ext}")
episode_pattern = FilePattern(filename_pattern="/episode{ext}")


# Create your models here.


class EpisodeModel(models.Model):
    episode_number = models.BigIntegerField(default=0)
    episode_name = models.CharField(max_length=1024, db_index=True)
    episode_cover = models.ImageField(
        storage=OverwriteStorage(),
        upload_to=episode_cover,
        default=None,
        blank=True,
        null=True,
    )
    episode_file = models.FileField(
        storage=OverwriteStorage(),
        upload_to=episode_pattern,
        default=None,
        blank=True,
        null=True,
    )
    episode_summary = models.TextField(default="", blank=True, null=True)

    episode_comments = models.ManyToManyField(EpisodeCommentModel, blank=True)
    episode_timestamps = models.ManyToManyField(EpisodeTimestampModel, blank=True)

    def __str__(self) -> str:
        return f"{self.episode_number}. {self.episode_name}"

    class Meta:
        verbose_name = "Episode"
