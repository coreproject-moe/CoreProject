from django.db import models
from colorfield.fields import ColorField


class BackgroundColorMixin(models.Model):
    # This will be initially null before being added by celery
    background_color = ColorField(null=True, blank=True)

    class Meta:
        abstract = True
