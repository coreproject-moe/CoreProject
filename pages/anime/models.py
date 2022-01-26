from django.db import models

# Create your models here.


class AnimeDetailsPage(models.Model):
    anime_picture = models.ImageField()


class AnimeEpisode(models.Model):
    anime_episode = models.FileField()
