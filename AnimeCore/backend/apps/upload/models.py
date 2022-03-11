from pathlib import Path
from uuid import uuid4
from django.db import models


class FileField:
    # Thanks Stackoverflow
    # https://stackoverflow.com/questions/1190697/django-filefield-with-upload-to-determined-at-runtime
    @staticmethod
    def anime_cover(instance, filename) -> str:
        return Path("anime", instance.anime_name, filename)

    @staticmethod
    def episode_cover(instance, filename) -> str:
        return Path("episode_cover", filename)

    @staticmethod
    def episode_upload(instance, filename) -> str:
        return Path("episode", filename)


# Create your models here.


class EpisodeModel(models.Model):
    episode_number = models.BigAutoField(primary_key=True)
    episode_name = models.CharField(max_length=1024)
    episode_cover = models.ImageField(
        upload_to=FileField.episode_cover, default=None, blank=True, null=True
    )
    episode_file = models.FileField(
        upload_to=FileField.episode_upload, default=None, blank=True, null=True
    )
    episode_summary = models.TextField(default="", blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.episode_number}. {self.episode_name}"


class AnimeInfoModel(models.Model):
    anime_name = models.CharField(max_length=1024)
    anime_cover = models.ImageField(
        upload_to=FileField.anime_cover, default=None, blank=True, null=True
    )
    episodes = models.ManyToManyField(EpisodeModel)

    def __str__(self) -> str:
        return f"{self.anime_name}"
