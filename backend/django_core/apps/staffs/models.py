from core.storages import OverwriteStorage
from django.db import models
from dynamic_filenames import FilePattern

staff_upload_pattern = FilePattern(filename_pattern="staffs/{uuid:s}{ext}")


# Create your models here.
class StaffAlternateNameModel(models.Model):
    name = models.CharField(max_length=1024, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class StaffModel(models.Model):
    mal_id = models.IntegerField(unique=True, null=True, blank=True, db_index=True)
    kitsu_id = models.IntegerField(unique=True, null=True, blank=True, db_index=True)
    anilist_id = models.IntegerField(unique=True, null=True, blank=True, db_index=True)

    name = models.CharField(max_length=1024, db_index=True)
    given_name = models.CharField(max_length=1024, null=True, blank=True)
    family_name = models.CharField(max_length=1024, null=True, blank=True)

    staff_image = models.ImageField(
        storage=OverwriteStorage,
        upload_to=staff_upload_pattern,
        default=None,
        blank=True,
        null=True,
    )
    about = models.TextField(null=True, blank=True)
    alternate_names = models.ManyToManyField(StaffAlternateNameModel)

    def __str__(self) -> str:
        return f"{self.pk}. {self.name}"

    class Meta:
        verbose_name = "Staff | People"
        verbose_name_plural = "Staffs | Peoples"
