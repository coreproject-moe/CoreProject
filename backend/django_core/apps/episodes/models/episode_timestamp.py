from django.contrib.auth import get_user_model
from django.db import models
from mixins.models.created_at import CreatedAtMixin

# Create your models here.


class EpisodeTimestampModel(CreatedAtMixin):
    timestamp = models.IntegerField(default=0)

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.episode}. {self.user}"

    class Meta:
        verbose_name = "Episode Timestamp"
