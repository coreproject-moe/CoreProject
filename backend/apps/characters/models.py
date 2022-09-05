from pathlib import Path
from typing import Any

from django.db import models
from core.storages import OverwriteStorage


class FileField:
    # Thanks Stackoverflow
    # https://stackoverflow.com/questions/1190697/django-filefield-with-upload-to-determined-at-runtime
    @staticmethod
    def anime_charater(instance: Any, filename: str) -> Path:
        return Path("anime_characters", filename)


# Create your models here.


class CharacterModel(models.Model):
    mal_id = models.IntegerField(unique=True, null=True, db_index=True)
    kitsu_id = models.IntegerField(unique=True, null=True, db_index=True)
    anilist_id = models.IntegerField(unique=True, null=True, db_index=True)

    name = models.CharField(max_length=1024, db_index=True)
    name_kanji = models.CharField(max_length=1024, null=True, blank=True, db_index=True)
    character_image = models.ImageField(
        upload_to=FileField.anime_charater,
        storage=OverwriteStorage(),
        default=None,
        blank=True,
        null=True,
    )
    about = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.mal_id}. {self.name}"

    class Meta:
        verbose_name = "Character"
        verbose_name_plural = "Characters"
