from apps.user.models import CustomUser

from django.db import models

from ..managers import EpisodeCommentManager
from treebeard.mp_tree import MP_Node

# Create your models here.


class EpisodeCommentModel(MP_Node):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()

    comment_added = models.DateTimeField(auto_now=True)
    objects = EpisodeCommentManager()

    node_order_by = ["comment_added"]

    def __str__(self) -> str:
        return f"{self.user} | {self.text}"

    class Meta:
        verbose_name = "Episode Comment"
