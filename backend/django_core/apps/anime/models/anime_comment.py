from colorfield.fields import ColorField
from django.contrib.postgres.indexes import GinIndex
from django.db import models
from dynamic_filenames import FilePattern
from mixins.models.created_at import CreatedAtMixin
from mixins.models.is_locked import IsLockedMixin
from mixins.models.updated_at import UpdatedAtMixin
from django_ltree.models import TreeModel
from django.contrib.postgres import indexes as idx

from apps.user.models import CustomUser
from ...characters.models import CharacterModel
from ...episodes.models import EpisodeModel
from ...producers.models import ProducerModel
from ...staffs.models import StaffModel
from .anime_genre import AnimeGenreModel
from .anime_openings_and_endings import AnimeEndingModel, AnimeOpeningModel
from .anime_theme import AnimeThemeModel
class AnimeCommentModel(CreatedAtMixin, TreeModel):
    label_size = 4
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self) -> str:
        return f"{self.user} | {self.text}"

    class Meta:
        # https://youtu.be/u8F7bTJVe_4?t=1051
        indexes = [idx.GistIndex(fields=["path"])]
        verbose_name = "Anime Comment"
        verbose_name_plural = "Anime Comments"
