from apps.user.models import CustomUser
from django.db import models
from mixins.models.created_at import CreatedAtMixin
from treenode.models import TreeNodeModel

# Create your models here.


class EpisodeCommentModel(TreeNodeModel, CreatedAtMixin):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self) -> str:
        return f"{self.user} | {self.text}"

    class Meta:
        # https://youtu.be/u8F7bTJVe_4?t=1057
        indexes = [idx.GistIndex(fields=["path"])]
