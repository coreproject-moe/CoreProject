from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class EpisodeCommentModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()

    comment_added = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user} | {self.text}"

    class Meta:
        verbose_name = "Episode Comment"
