from django.db import models

from .anime_info import AnimeInfoModel

# Create your models here.


class AnimeRecommendationModel(models.Model):
    entry = models.ForeignKey(
        to=AnimeInfoModel,
        related_name="entry",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    anime = models.ForeignKey(
        to=AnimeInfoModel,
        related_name="anime",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    mal_url = models.URLField(unique=True)

    def __str__(self) -> str:
        return f"{self.entry}"

    class Meta:
        verbose_name = "Anime Recommendation"
