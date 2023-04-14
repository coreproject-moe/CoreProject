from django.db import models


class BrightnessMixin(models.Model):
    brightness = models.FloatField()

    class Meta:
        abstract = True
