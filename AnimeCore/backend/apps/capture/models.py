import datetime

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator

from apps.upload.models import EpisodeModel, AnimeInfoModel

# Create your models here.


class CaptureEpisodeModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    episode = models.ForeignKey(EpisodeModel, on_delete=models.CASCADE)
    timestamp = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self) -> str:
        return f"Episode No : {self.episode.episode_number} | Time stamp = {datetime.timedelta(seconds=self.timestamp)} | User : {self.user.username}"

    class Meta:
        verbose_name = "Episode"
        ordering = ("id",)


class CaptureAnimeNameModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    anime = models.ForeignKey(AnimeInfoModel, on_delete=models.CASCADE)
    episodes = models.ManyToManyField(CaptureEpisodeModel, blank=True)

    def __str__(self) -> str:
        return f"Anime : {self.anime} | User : {self.user.username}"

    class Meta:
        verbose_name = "Anime"
        ordering = ("id",)


class CaptureInfoModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    video_volume = models.PositiveIntegerField(
        default=100,
        validators=[
            MaxValueValidator(100),
        ],
    )

    video_timestamps = models.ManyToManyField(CaptureAnimeNameModel, blank=True)

    def __str__(self) -> str:
        return f"User = {self.user.username} | Volume = {self.video_volume} | Total Stamps = {self.video_timestamps.all().count()}"

    class Meta:
        verbose_name = "Master"
        ordering = ("user",)
