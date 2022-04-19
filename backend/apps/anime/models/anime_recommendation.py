from django.db import models

from .anime_info import AnimeInfoModel

# Create your models here.


class AnimeRecommendationModel(models.Model):
    entry = models.ForeignKey(
        to=AnimeInfoModel, on_delete=models.SET_NULL, null=True, blank=True
    )
    anime = models.IntegerField(db_index=True)
    mal_url = models.URLField(unique=True)

    def __str__(self) -> str:
        return f"{self.entry}"

    class Meta:
        verbose_name = "Anime Recommendation"
