from django.db import models

# Create your models here.


class AnimeThemeModel(models.Model):
    mal_id = models.IntegerField(
        unique=True, blank=False, null=False, primary_key=True, db_index=True
    )
    name = models.CharField(
        unique=True, max_length=50, default="", null=False, blank=False, db_index=True
    )
    type = models.CharField(
        max_length=50, default="", null=False, blank=False, db_index=True
    )

    def __str__(self) -> str:
        return f"{self.mal_id}. {self.name} ({self.type})"

    class Meta:
        verbose_name = "Anime Theme"
