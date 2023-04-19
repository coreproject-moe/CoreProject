from mixins.models.created_at import CreatedAtMixin
from mixins.models.updated_at import UpdatedAtMixin

from django.db import models

# Create your models here.


class ProducerModel(CreatedAtMixin, UpdatedAtMixin):
    mal_id = models.IntegerField(unique=True, blank=True, null=True)
    kitsu_id = models.IntegerField(unique=True, blank=True, null=True)
    name = models.CharField(
        max_length=128,
        default="",
        null=False,
        blank=False,
    )
    # Titles
    japanese_title = models.CharField(
        max_length=128,
        default="",
        null=True,
        blank=True,
    )
    established = models.DateTimeField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.pk}. {self.name} | Mal_id : {self.mal_id}"

    class Meta:
        verbose_name = "Producer"
        verbose_name_plural = "Producers"
