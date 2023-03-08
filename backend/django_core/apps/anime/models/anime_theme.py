from django.db import models

# Create your models here.

TYPE_CHOICES = [
    ("Anime", "anime"),
    ("Manga", "manga"),
]


class AnimeThemeModel(models.Model):
    mal_id = models.IntegerField(unique=True, blank=False, null=False)
    name = models.CharField(unique=True, max_length=50, default="", null=False, blank=False)
    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        default="",
        null=False,
        blank=False,
    )

    def __str__(self) -> str:
        return f"{self.pk}. {self.name} ({self.type})"

    class Meta:
        verbose_name = "Anime Theme"
