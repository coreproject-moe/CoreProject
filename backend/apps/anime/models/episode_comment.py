from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class EpisodeCommentModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment_added = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __str__(self) -> str:
        return f"{self.user}"

    class Meta:
        verbose_name = "Episode Comment"
        # Sort by newest first
        ordering = ("-comment_added",)
