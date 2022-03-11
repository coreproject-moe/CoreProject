import datetime

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.upload.models import EpisodeModel, AnimeInfoModel

# Create your models here.


class CaptureEpisodeModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    episode = models.ForeignKey(EpisodeModel, on_delete=models.CASCADE)
    timestamp = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self) -> str:
        return f"Episode : {self.episode.episode_number} | Time stamp = {datetime.timedelta(seconds=self.timestamp)} | User : {self.user.username}"


class CaptureAnimeNameModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    anime = models.ForeignKey(AnimeInfoModel, on_delete=models.CASCADE)
    episdoes = models.ManyToManyField(CaptureEpisodeModel)

    def __str__(self) -> str:
        return f"Anime : {self.anime} | User : {self.user.username}"


class CaptureVideoModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    video_volume = models.IntegerField(
        default=50,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0),
        ],
    )

    timestamp = models.ManyToManyField(CaptureAnimeNameModel)

    def __str__(self) -> str:
        return f"User = {self.user.username} | Video Volume = {self.video_volume}"

    class Meta:
        verbose_name = "User Video Capture Model"
