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

    class Meta(TreeNodeModel.Meta):
        verbose_name = "Episode Comment"
        verbose_name_plural = "Episode Comments"
