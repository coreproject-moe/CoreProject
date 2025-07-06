from django.db import models


class IsLockedMixin(models.Model):
    is_locked = models.BooleanField(db_default=False)

    class Meta:
        abstract = True
