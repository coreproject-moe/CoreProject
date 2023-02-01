from django.db import models

# Create your models here.


class AnimeThemeModel(models.Model):
    mal_id = models.IntegerField(unique=True, blank=False, null=False)
    name = models.CharField(unique=True, max_length=50, default="", null=False, blank=False)
    type = models.CharField(max_length=50, default="", unique=True, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.pk}. {self.name} ({self.type})"

    class Meta:
        verbose_name = "Anime Theme"
