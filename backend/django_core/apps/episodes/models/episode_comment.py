from apps.user.models import CustomUser

from django.db import models

from ..managers import EpisodeCommentManager

# Create your models here.


class EpisodeCommentModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()

    comment_added = models.DateTimeField(auto_now=True)

    objects = EpisodeCommentManager()

    def __str__(self) -> str:
        return f"{self.user} | {self.text}"

    class Meta:
        verbose_name = "Episode Comment"
