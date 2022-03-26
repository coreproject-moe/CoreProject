from pathlib import Path


from django.db import models
from django.contrib.auth import get_user_model


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
        verbose_name = "User Comment"
        # Sort by newest first
        ordering = ("-comment_added",)


class EpisodeTimestampModel(models.Model):
    timestamp = models.IntegerField(default=0)
    episode_number = models.IntegerField(null=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} | {self.timestamp}"

    class Meta:
        verbose_name = "User Timestamp"


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
    episode_timestamps = models.ManyToManyField(EpisodeTimestampModel, blank=True)

    def __str__(self) -> str:
        return f"{self.episode_number}. {self.episode_name}"

    class Meta:
        verbose_name = "Episode"
        ordering = ("id",)


class AnimeInfoModel(models.Model):
    mal_id = models.IntegerField(unique=True, blank=False, null=False, primary_key=True)
    anime_name = models.CharField(max_length=1024)
    anime_name_japanese = models.CharField(max_length=1024, null=True)
    anime_source = models.CharField(max_length=128, blank=True, null=True)
    anime_aired_from = models.DateTimeField(blank=True, null=True)
    anime_aired_to = models.DateTimeField(blank=True, null=True)
    anime_cover = models.ImageField(
        upload_to=FileField.anime_cover, default=None, blank=True, null=True
    )
    anime_synopsis = models.TextField(blank=True, null=True)
    anime_background = models.TextField(blank=True, null=True)
    anime_rating = models.CharField(max_length=50, blank=True, null=True)

    episodes = models.ManyToManyField(EpisodeModel, blank=True)
    updated = models.DateTimeField(auto_now_add=True)

    # anime_rating = models.CharField(max_length=128)
    # genres = models.ManyToManyField(blank=True)
    def __str__(self) -> str:
        return f"{self.anime_name}"

    class Meta:
        verbose_name = "Anime"
        ordering = ("mal_id",)
