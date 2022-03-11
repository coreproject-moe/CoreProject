from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class CaptureVideoVolumeModel(models.Model):
    user = models.OneToOneField(
        get_user_model(), related_name="user", on_delete=models.CASCADE
    )
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
        verbose_name = "User Info Capture Model"


class CaptureVideoTimeStampModel(models.Model):
    pass
