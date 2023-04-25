from django.db import models


class IsLockedMixin(models.Model):
    is_locked = models.BooleanField(default=False)

    class Meta:
        abstract = True
