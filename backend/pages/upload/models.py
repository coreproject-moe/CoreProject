from django.db import models

# Create your models here.


class AnimeNameModel(models.Model):
    anime_name = models.CharField(max_length=1024)
    anime_cover = models.ImageField(
        upload_to="anime", default=None, blank=True, null=True
    )
