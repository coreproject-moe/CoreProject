from core.storages import OverwriteStorage
from mixins.created_at import CreatedAtMixin
from mixins.updated_at import UpdatedAtMixin

from ..images.models import Image
from django.db import models


class StaffAlternateNameModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Staff | People ( Alternate Name )"
        verbose_name_plural = "Staff | People ( Alternate Names )"


class StaffModel(CreatedAtMixin, UpdatedAtMixin):
    mal_id = models.IntegerField(unique=True, null=True, blank=True)
    kitsu_id = models.IntegerField(unique=True, null=True, blank=True)
    anilist_id = models.IntegerField(unique=True, null=True, blank=True)

    name = models.CharField(max_length=1024)
    given_name = models.CharField(max_length=1024, null=True, blank=True)
    family_name = models.CharField(max_length=1024, null=True, blank=True)
    alternate_names = models.ManyToManyField(StaffAlternateNameModel, blank=True)

    staff_image = models.ForeignKey(Image, on_delete=models.CASCADE)
    about = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.pk}. {self.name}"

    class Meta:
        verbose_name = "Staff | People"
        verbose_name_plural = "Staffs | Peoples"
