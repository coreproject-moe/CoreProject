from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class EpisodeTimestampModel(models.Model):
    timestamp = models.IntegerField(default=0)
    episode_number = models.IntegerField(null=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, db_index=True)

    def __str__(self) -> str:
        return f"{self.episode_number}. {self.user}"

    class Meta:
        verbose_name = "Episode Timestamp"
