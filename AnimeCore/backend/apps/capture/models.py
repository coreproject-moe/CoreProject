from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class CaptureVolumeModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    video_volume = models.PositiveIntegerField(
        default=100,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )

    def __str__(self) -> str:
        return f"User = {self.user.username} | Total Stamps = {self.video_volume}"

    class Meta:
        verbose_name = "Master Volumes"
        ordering = ("user",)
