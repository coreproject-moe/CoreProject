from mixins.created_at import CreatedAtMixin
from mixins.updated_at import UpdatedAtMixin
from ..images.models import Image
from django.db import models


# Create your models here.


class CharacterModel(CreatedAtMixin, UpdatedAtMixin):
    mal_id = models.IntegerField(unique=True, null=True)
    kitsu_id = models.IntegerField(unique=True, null=True)
    anilist_id = models.IntegerField(unique=True, null=True)

    name = models.CharField(max_length=1024)
    name_kanji = models.CharField(max_length=1024, null=True, blank=True)
    character_image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    about = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.pk}. {self.name}"

    class Meta:
        verbose_name = "Character"
        verbose_name_plural = "Characters"
