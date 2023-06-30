from django.db import models
from mixins.models.created_at import CreatedAtMixin
from mixins.models.is_locked import IsLockedMixin
from mixins.models.updated_at import UpdatedAtMixin

# Create your models here.


class ProducerModel(CreatedAtMixin, UpdatedAtMixin, IsLockedMixin):
    # Ids
    mal_id = models.IntegerField(unique=True, blank=True, null=True)
    kitsu_id = models.IntegerField(unique=True, blank=True, null=True)

    # Titles
    name = models.CharField(
        max_length=128,
        default="",
        null=False,
        blank=False,
    )
    name_japanese = models.CharField(
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
