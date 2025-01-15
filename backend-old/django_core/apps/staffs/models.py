from core.storages import OverwriteStorage
from django.contrib.postgres.indexes import GinIndex
from django.db import models
from dynamic_filenames import FilePattern
from mixins.models.created_at import CreatedAtMixin
from mixins.models.is_locked import IsLockedMixin
from mixins.models.updated_at import UpdatedAtMixin

staff_upload_pattern = FilePattern(filename_pattern="staffs/{uuid:s}{ext}")


class StaffAlternateNameModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        indexes = [
            GinIndex(
                name="staff_alternate_idx",
                fields=["name"],
                opclasses=["gin_trgm_ops"],
            ),
        ]
        verbose_name = "Staff | People ( Alternate Name )"
        verbose_name_plural = "Staff | People ( Alternate Names )"


class StaffModel(CreatedAtMixin, UpdatedAtMixin, IsLockedMixin):
    mal_id = models.IntegerField(unique=True, null=True, blank=True)
    kitsu_id = models.IntegerField(unique=True, null=True, blank=True)
    anilist_id = models.IntegerField(unique=True, null=True, blank=True)

    name = models.CharField(max_length=1024)
    given_name = models.CharField(max_length=1024, null=True, blank=True)
    family_name = models.CharField(max_length=1024, null=True, blank=True)
    alternate_names = models.ManyToManyField(StaffAlternateNameModel, blank=True)

    staff_image = models.ImageField(
        storage=OverwriteStorage,
        upload_to=staff_upload_pattern,
        default=None,
        blank=True,
        null=True,
    )
    about = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.pk}. {self.name}"

    class Meta:
        indexes = [
            GinIndex(
                fields=["name", "given_name", "family_name"],
                name="staff_name_idx",
                opclasses=["gin_trgm_ops", "gin_trgm_ops", "gin_trgm_ops"],
            ),
        ]
        verbose_name = "Staff | People"
        verbose_name_plural = "Staffs | Peoples"
