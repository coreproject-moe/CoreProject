from dynamic_filenames import FilePattern

from django.db import models

anime_charaters_pattern = FilePattern(filename_pattern="characters/{uuid:s}{ext}")


# Create your models here.


class CharacterModel(models.Model):
    mal_id = models.IntegerField(unique=True, null=True)
    kitsu_id = models.IntegerField(unique=True, null=True)
    anilist_id = models.IntegerField(unique=True, null=True)

    name = models.CharField(max_length=1024)
    name_kanji = models.CharField(max_length=1024, null=True, blank=True)
    character_image = models.ImageField(
        upload_to=anime_charaters_pattern,
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
