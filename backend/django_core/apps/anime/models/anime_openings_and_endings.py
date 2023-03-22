from django.db import models
from dynamic_filenames import FilePattern


opening_upload_pattern = FilePattern(filename_pattern="opening/{uuid:s}{ext}")
ending_upload_pattern = FilePattern(filename_pattern="ending/{uuid:s}{ext}")


# Create your models here.
class AbstractBaseModel(models.Model):
    # Either opening number/closing number
    entry = models.BigIntegerField(null=False, blank=False)
    # Opening/closing theme name
    name = models.CharField(max_length=512, blank=False, null=False)

    class Meta:
        unique_together = [
            ("entry", "name"),
        ]
        abstract = True


class AnimeOpeningModel(AbstractBaseModel):
    thumbnail = models.ImageField(
        upload_to=opening_upload_pattern,
        default=None,
        blank=True,
        null=True,
    )


class AnimeEndingModel(AbstractBaseModel):
    thumbnail = models.ImageField(
        upload_to=ending_upload_pattern,
        default=None,
        blank=True,
        null=True,
    )
