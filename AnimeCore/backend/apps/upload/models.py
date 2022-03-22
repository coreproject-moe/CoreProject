from pathlib import Path
from re import A
from django.contrib.auth import get_user_model
from django.db import models


class FileField:
    # Thanks Stackoverflow
    # https://stackoverflow.com/questions/1190697/django-filefield-with-upload-to-determined-at-runtime
    @staticmethod
    def anime_cover(instance, filename) -> str:
        return Path("anime_cover", filename)

    @staticmethod
    def episode_cover(instance, filename) -> str:
        return Path("episode_cover", filename)

    @staticmethod
    def episode_upload(instance, filename) -> str:
        return Path("episode", filename)


# Create your models here.


class EpisodeCommentModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment_added = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __str__(self) -> str:
        return f"{self.user}"

    class Meta:
        verbose_name = "User comment"
        # Sort by newest first
        ordering = ("-comment_added",)


class EpisodeModel(models.Model):
    episode_number = models.BigIntegerField(default=0)
    episode_name = models.CharField(max_length=1024)
    episode_cover = models.ImageField(
        upload_to=FileField.episode_cover, default=None, blank=True, null=True
    )
    episode_file = models.FileField(
        upload_to=FileField.episode_upload, default=None, blank=True, null=True
    )
    episode_summary = models.TextField(default="", blank=True, null=True)
    episode_comments = models.ManyToManyField(EpisodeCommentModel, blank=True)

    def __str__(self) -> str:
        return f"{self.episode_number}. {self.episode_name}"

    class Meta:
        verbose_name = "Episode info"
        ordering = ("id",)


class AnimeInfoModel(models.Model):
    mal_id = models.IntegerField(unique=True, blank=False, null=False)
    anime_name = models.CharField(max_length=1024)
    anime_name_japanese = models.CharField(max_length=1024)
    anime_source = models.CharField(max_length=128)
    anime_aired_from = models.DateTimeField()
    anime_aired_to = models.DateTimeField()
    anime_cover = models.ImageField(
        upload_to=FileField.anime_cover, default=None, blank=True, null=True
    )
    # anime_rating = models.CharField(max_length=128)
    # genres = models.ManyToManyField(blank=True)
    episodes = models.ManyToManyField(EpisodeModel, blank=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.anime_name}"

    class Meta:
        verbose_name = "Anime"
        ordering = ("-mal_id",)
