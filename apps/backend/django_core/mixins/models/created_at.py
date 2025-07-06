from django.db import models
from django.db.models.functions import Now


class CreatedAtMixin(models.Model):
    created_at = models.DateTimeField(db_default=Now())

    class Meta:
        abstract = True
