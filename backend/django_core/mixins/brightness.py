from django.db import models


class BrightnessMixin(models.Model):
    # This will be initially null before being added by celery
    brightness = models.FloatField(null=True,blank=True)

    class Meta:
        abstract = True
