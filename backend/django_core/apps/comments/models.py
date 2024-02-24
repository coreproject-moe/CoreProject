from apps.user.models import CustomUser
from django.contrib.postgres import indexes as idx
from django.db import models
from django_ltree.models import TreeModel
from mixins.models.created_at import CreatedAtMixin


# Create your models here.


class CommentModel(CreatedAtMixin, TreeModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()

    upvotes = models.ManyToManyField(CustomUser, blank=True, related_name="upvotes")
    downvotes = models.ManyToManyField(CustomUser, blank=True, related_name="downvotes")

    deleted = models.BooleanField(default=False)

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

class ReportedCommentModel(CreatedAtMixin, models.Model):
    comment = models.ForeignKey(CommentModel, on_delete=models.CASCADE, null=True, blank=True)
    reports = models.ManyToManyField(CustomUser, blank=True, related_name="reports")

    @property
    def reports_count(self) -> int:
        return self.reports.count()

    def __str__(self) -> str:
        return f"Comment by {self.comment.user} | {self.reports_count} reports"

    class Meta:
        verbose_name = "Reported Comment"
        verbose_name_plural = "Reported Comments"