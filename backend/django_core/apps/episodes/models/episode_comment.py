from apps.user.models import CustomUser
from django.contrib.postgres import indexes as idx
from django.db import models
from django_ltree.models import TreeModel
from mixins.models.created_at import CreatedAtMixin

# Create your models here.


class EpisodeCommentModel(TreeModel, CreatedAtMixin):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self) -> str:
        return f"{self.user} | {self.text}"

    class Meta:
        indexes = [idx.GistIndex(fields=["path"])]
