from django.db import models

# Create your models here.


class AnimeInfoModel(models.Model):
    anime_name = models.CharField(max_length=1024)
    anime_cover = models.ImageField(
        upload_to="anime", default=None, blank=True, null=True
    )

    def __str__(self) -> str:
        return f"{self.anime_name}"


class EpisodeModel(models.Model):
    episode_number = models.BigAutoField(primary_key=True)
    episode_name = models.CharField(max_length=1024)
    episode_cover = models.ImageField(
        upload_to="episode_cover", default=None, blank=True, null=True
    )
    episode_file = models.FileField(
        upload_to="episode", default=None, blank=True, null=True
    )

    # Many to one relationship
    anime_name = models.ForeignKey(
        AnimeInfoModel, on_delete=models.CASCADE, default=None
    )

    def __str__(self) -> str:
        return f"{self.episode_number}. {self.episode_name}"
