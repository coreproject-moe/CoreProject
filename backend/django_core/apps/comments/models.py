from apps.user.models import CustomUser
from django.contrib.postgres import indexes as idx
from django.db import models
from django_ltree.models import TreeModel
from mixins.models.created_at import CreatedAtMixin

# Create your models here.


class CommentModel(CreatedAtMixin, TreeModel):
    label_size = 4
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()

    upvotes = models.ManyToManyField(CustomUser, blank=True, related_name="upvotes")
    downvotes = models.ManyToManyField(CustomUser, blank=True, related_name="downvotes")

    @property
    def ratio(self) -> int:
        # Formula : <like> - <dislike>
        return self.upvotes.count() - self.downvotes.count()

    @property
    def childrens(self) -> int:
        return self.children().count()

    def __str__(self) -> str:
        return f"{self.user} | {self.text}"

    class Meta:
        # https://youtu.be/u8F7bTJVe_4?t=1051
        indexes = [idx.GistIndex(fields=["path"])]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
