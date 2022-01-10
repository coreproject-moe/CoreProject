from django.db import models
from tinymce.models import HTMLField


class PageModel(models.Model):
    content = HTMLField()

    def __str__(self) -> str:
        return "Content"

    class Meta:
        verbose_name = "Page"
