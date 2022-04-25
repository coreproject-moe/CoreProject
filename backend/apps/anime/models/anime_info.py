from pathlib import Path
from django.db import models

from .episode import EpisodeModel
from .anime_genre import AnimeGenreModel
from .anime_theme import AnimeThemeModel
from .anime_studio import AnimeStudioModel
from .anime_producer import AnimeProducerModel
from .anime_synonym import AnimeSynonymModel


class FileField:
    # Thanks Stackoverflow
    # https://stackoverflow.com/questions/1190697/django-filefield-with-upload-to-determined-at-runtime
    @staticmethod
    def anime_cover(instance, filename: str) -> str:
        return Path("anime_cover", filename)

    @staticmethod
    def anime_charater(instance, filename: str) -> str:
        return Path("anime_characters", filename)

    @staticmethod
    def anime_banner(instance, filename: str) -> str:
        return Path("anime_banner", filename)


# Create your models here.


class AnimeInfoModel(models.Model):
    mal_id = models.IntegerField(unique=True, blank=False, null=False)
    # anilist_id = models.IntegerField(unique=True, blank=False, null=False)
    anime_name = models.CharField(unique=True, max_length=1024, db_index=True)
    anime_name_japanese = models.CharField(max_length=1024, null=True, db_index=True)
    anime_source = models.CharField(max_length=128, blank=True, null=True)
    anime_aired_from = models.DateTimeField(blank=True, null=True)
    anime_aired_to = models.DateTimeField(blank=True, null=True)
    anime_banner = models.ImageField(
        upload_to=FileField.anime_banner, default=None, blank=True, null=True
    )
    anime_cover = models.ImageField(
        upload_to=FileField.anime_cover, default=None, blank=True, null=True
    )
    anime_synopsis = models.TextField(blank=True, null=True)
    anime_background = models.TextField(blank=True, null=True)
    anime_rating = models.CharField(max_length=50, blank=True, null=True)

    anime_genres = models.ManyToManyField(AnimeGenreModel, blank=True)
    anime_themes = models.ManyToManyField(AnimeThemeModel, blank=True)
    anime_studios = models.ManyToManyField(AnimeStudioModel, blank=True)
    anime_producers = models.ManyToManyField(AnimeProducerModel, blank=True)
    anime_name_synonyms = models.ManyToManyField(AnimeSynonymModel, blank=True)
    anime_episodes = models.ManyToManyField(EpisodeModel, blank=True)
    anime_recommendation = models.ManyToManyField("AnimeInfoModel", blank=True)

    updated = models.DateTimeField(auto_now_add=True)

    # anime_rating = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.anime_name}"

    class Meta:
        verbose_name = "Anime"
