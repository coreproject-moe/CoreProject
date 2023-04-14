from django.db import models
from colorfield.fields import ColorField


class BackgroundColorMixin(models.Model):
    background_color = ColorField()

    class Meta:
        abstract = True
