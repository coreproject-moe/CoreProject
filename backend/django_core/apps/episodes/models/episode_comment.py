from apps.user.models import CustomUser

from django.db import models

from treenode.models import TreeNodeModel

# Create your models here.


class EpisodeCommentModel(TreeNodeModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()

    comment_added = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user} | {self.text}"

    class Meta(TreeNodeModel.Meta):
        verbose_name = "Episode Comment"
        verbose_name_plural = "Episode Comments"
