from apps.user.managers import UsernameWithDiscriminatorManager

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class EpisodeTimestampModel(models.Model):
    timestamp = models.IntegerField(default=0)

    episode = models.ForeignKey(
        to="EpisodeModel",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    objects = UsernameWithDiscriminatorManager()

    def __str__(self) -> str:
        return f"{self.episode}. {self.user}"

    class Meta:
        verbose_name = "Episode Timestamp"
