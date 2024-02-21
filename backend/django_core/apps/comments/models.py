from apps.user.models import CustomUser
from django.contrib.postgres import indexes as idx
from django.db import models
from django_ltree.models import TreeModel
from mixins.models.created_at import CreatedAtMixin
from django.core.validators import RegexValidator
from django_ltree.fields import PathField
from django import forms
from django.forms.widgets import TextInput

path_label_validator = RegexValidator(
    r"(?P<root>[a-zA-Z][a-zA-Z0-9_]*|\d+)(?:\.[a-zA-Z0-9_]+)*$",
    "A label is a sequence of alphanumeric characters and underscores separated by dots.",
    "invalid",
)

# Monkeypatch things


class FixedPathFormField(forms.CharField):
    default_validators = [path_label_validator]


class FixedPathField(PathField):
    default_validators = [path_label_validator]

    def formfield(self, **kwargs):
        kwargs["form_class"] = FixedPathFormField
        kwargs["widget"] = TextInput(attrs={"class": "vTextField"})
        return super(PathField, self).formfield(**kwargs)

    class Meta:
        abstract = True


class FixedTreeModel(TreeModel):
    path = FixedPathField()

    class Meta:
        abstract = True


# Create your models here.


class CommentModel(CreatedAtMixin, FixedTreeModel):
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
