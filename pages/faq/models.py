from django.db import models
from tinymce.models import HTMLField


class PageModel(models.Model):
    content = HTMLField()
