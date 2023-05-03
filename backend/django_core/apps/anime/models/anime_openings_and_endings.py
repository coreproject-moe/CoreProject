from django.db import models
from dynamic_filenames import FilePattern

opening_upload_pattern = FilePattern(filename_pattern="opening/{uuid:s}{ext}")
ending_upload_pattern = FilePattern(filename_pattern="ending/{uuid:s}{ext}")


# Create your models here.


class AbstractBaseOpeningAndEndingModel(models.Model):
    # Either opening number/closing number
    entry = models.BigIntegerField(null=False, blank=False)
    # Opening/closing theme name
    name = models.CharField(max_length=512, blank=False, null=False)
    # Canonical URL
    url = models.URLField(blank=False, null=True)

    class Meta:
        abstract = True


class AnimeOpeningModel(AbstractBaseOpeningAndEndingModel):
    thumbnail = models.ImageField(
        upload_to=opening_upload_pattern,
        default=None,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.entry}. {self.name}"

    class Meta:
        unique_together = [
            ("entry", "name", "url"),
        ]
        verbose_name = "Anime Opening"
        verbose_name_plural = "Anime Openings"


class AnimeEndingModel(AbstractBaseOpeningAndEndingModel):
    thumbnail = models.ImageField(
        upload_to=ending_upload_pattern,
        default=None,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.entry}. {self.name}"

    class Meta:
        unique_together = [
            ("entry", "name", "url"),
        ]
        verbose_name = "Anime Ending"
        verbose_name_plural = "Anime Endings"
