from django.db import models


# Create your models here.
class StaffAlternateNameModel(models.Model):
    name = models.CharField(max_length=1024, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class StaffModel(models.Model):
    mal_id = models.IntegerField(unique=True, db_index=True)
    kitsu_id = models.IntegerField(unique=True, null=True, db_index=True)
    anilist_id = models.IntegerField(unique=True, null=True, db_index=True)

    name = models.CharField(max_length=1024, db_index=True)
    given_name = models.CharField(max_length=1024, db_index=True)
    family_name = models.CharField(max_length=1024, db_index=True)

    about = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "People"
        verbose_name_plural = "Peoples"
