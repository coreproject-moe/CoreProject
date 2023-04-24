from django.db import models


class IsLockedMixin(models.Model):
    is_locked = models.BooleanField()

    class Meta:
        abstract = True
