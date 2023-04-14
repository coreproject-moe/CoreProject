from django.db import models
from ...images.models import Image


# Create your models here.
class AbstractBaseOpeningAndEndingModel(models.Model):
    # Either opening number/closing number
    entry = models.BigIntegerField(null=False, blank=False)
    # Opening/closing theme name
    name = models.CharField(max_length=512, blank=False, null=False)
    # Canonical URL
    url = models.URLField(blank=False, null=True)
    thumbnail = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


class AnimeOpeningModel(AbstractBaseOpeningAndEndingModel):
    def __str__(self) -> str:
        return f"{self.entry}. {self.name}"

    class Meta:
        unique_together = [
            ("entry", "name", "url"),
        ]
        verbose_name = "Anime Opening"
        verbose_name_plural = "Anime Openings"


class AnimeEndingModel(AbstractBaseOpeningAndEndingModel):
    def __str__(self) -> str:
        return f"{self.entry}. {self.name}"

    class Meta:
        unique_together = [
            ("entry", "name", "url"),
        ]
        verbose_name = "Anime Ending"
        verbose_name_plural = "Anime Endings"
