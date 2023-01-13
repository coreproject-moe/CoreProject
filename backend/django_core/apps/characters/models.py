from core.storages import OverwriteStorage
from django.db import models
from dynamic_filenames import FilePattern

anime_charaters_pattern = FilePattern(filename_pattern="anime_characters/{uuid:s}{ext}")


# Create your models here.


class CharacterModel(models.Model):
    mal_id = models.IntegerField(unique=True, null=True, db_index=True)
    kitsu_id = models.IntegerField(unique=True, null=True, db_index=True)
    anilist_id = models.IntegerField(unique=True, null=True, db_index=True)

    name = models.CharField(max_length=1024, db_index=True)
    name_kanji = models.CharField(max_length=1024, null=True, blank=True, db_index=True)
    character_image = models.ImageField(
        upload_to=anime_charaters_pattern,
        storage=OverwriteStorage(),
        default=None,
        blank=True,
        null=True,
    )
    about = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.pk}. {self.name}"

    class Meta:
        verbose_name = "Character"
        verbose_name_plural = "Characters"
