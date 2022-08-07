from pathlib import Path

from django.db import models


class FileField:
    # Thanks Stackoverflow
    # https://stackoverflow.com/questions/1190697/django-filefield-with-upload-to-determined-at-runtime
    @staticmethod
    def anime_charater(instance, filename) -> str:
        return Path("anime_characters", filename)


# Create your models here.


class CharacterModel(models.Model):
    mal_id = models.IntegerField(unique=True, db_index=True)
    name = models.CharField(max_length=1024, unique=True, db_index=True)
    character_image = models.ImageField(
        upload_to=FileField.anime_charater, default=None, blank=True, null=True
    )

    class Meta:
        verbose_name = "Anime Character"
