import datetime

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class CaptureVideoVolumeModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    video_volume = models.IntegerField(
        default=50,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0),
        ],
    )

    def __str__(self) -> str:
        return f"User = {self.user.username} | Video Volume = {self.video_volume}"

    class Meta:
        verbose_name = "User Video Volume Capture Model"


class CaptureVideoTimeStampModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    video_timestamp = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
        ],
    )

    def __str__(self) -> str:
        return f"User = {self.user.username} | Video Time stamp = {datetime.timedelta(self.video_volume)}"

    class Meta:
        verbose_name = "User Video Timestamp Capture Model"
