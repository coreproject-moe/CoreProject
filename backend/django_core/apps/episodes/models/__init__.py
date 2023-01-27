from core.storages import OverwriteStorage
from dynamic_filenames import FilePattern

from django.db import models

from .episode_comment import EpisodeCommentModel
from .episode_timestamp import EpisodeTimestampModel

episode_cover_pattern = FilePattern(filename_pattern="/episode_cover/{uuid:s}{ext}")
episode_pattern = FilePattern(filename_pattern="/episode/{uuid:s}{ext}")


# Create your models here.


class EpisodeModel(models.Model):
    episode_number = models.BigIntegerField(default=0)
    episode_name = models.CharField(max_length=1024)
    episode_cover = models.ImageField(
        storage=OverwriteStorage(),
        upload_to=episode_cover_pattern,
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
        verbose_name_plural = "Episodes"


from .episode_comment import EpisodeCommentModel as EpisodeCommentModel
from .episode_timestamp import EpisodeTimestampModel as EpisodeTimestampModel
