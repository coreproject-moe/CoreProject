from pathlib import Path
from typing import Any

from django.db import models

from core.storages import OverwriteStorage


class FileField:
    # Thanks Stackoverflow
    # https://stackoverflow.com/questions/1190697/django-filefield-with-upload-to-determined-at-runtime
    @staticmethod
    def staff(instance: Any, filename: str) -> Path:
        return Path("staff", filename)


# Create your models here.
class StaffAlternateNameModel(models.Model):
    name = models.CharField(max_length=1024, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class StaffModel(models.Model):
    mal_id = models.IntegerField(unique=True, null=True, db_index=True)
    kitsu_id = models.IntegerField(unique=True, null=True, db_index=True)
    anilist_id = models.IntegerField(unique=True, null=True, db_index=True)

    name = models.CharField(max_length=1024, db_index=True)
    given_name = models.CharField(max_length=1024, null=True)
    family_name = models.CharField(max_length=1024, null=True)

    staff_image = models.ImageField(
        storage=OverwriteStorage,
        upload_to=FileField.staff,
        default=None,
        blank=True,
        null=True,
    )
    about = models.TextField(null=True)
    alternate_names = models.ManyToManyField(StaffAlternateNameModel)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Staff | People"
        verbose_name_plural = "Staffs | Peoples"
