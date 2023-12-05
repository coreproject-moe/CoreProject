from colorfield.fields import ColorField
from django.contrib.postgres.indexes import GinIndex
from django.db import models
from dynamic_filenames import FilePattern
from mixins.models.created_at import CreatedAtMixin
from mixins.models.is_locked import IsLockedMixin
from mixins.models.updated_at import UpdatedAtMixin

from ...comments.models import CommentModel
from ...characters.models import CharacterModel
from ...episodes.models import EpisodeModel
from ...producers.models import ProducerModel
from ...staffs.models import StaffModel
from .anime_genre import AnimeGenreModel
from .anime_openings_and_endings import AnimeEndingModel, AnimeOpeningModel
from .anime_theme import AnimeThemeModel

cover_upload_pattern = FilePattern(filename_pattern="cover/{uuid:s}{ext}")
banner_upload_pattern = FilePattern(filename_pattern="banner/{uuid:s}{ext}")

# Create your models here.


class AnimeNameSynonymModel(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        indexes = [
            GinIndex(
                name="anime_name_synonym_idx", fields=["name"], opclasses=["gin_trgm_ops"]
            ),
        ]
        verbose_name = "Anime Synonym"


class AnimeModel(CreatedAtMixin, UpdatedAtMixin, IsLockedMixin):
    mal_id = models.IntegerField(unique=True, blank=True, null=True)
    anilist_id = models.IntegerField(unique=True, blank=True, null=True)
    kitsu_id = models.IntegerField(unique=True, blank=True, null=True)

    # These 3 fields can't be null or else search vector will throw an error
    name = models.CharField(
        unique=True,
        null=False,
        max_length=1024,
        db_index=True,
    )
    name_japanese = models.CharField(
        default="",
        null=False,
        blank=True,
        max_length=1024,
        db_index=True,
    )
    name_synonyms = models.ManyToManyField(AnimeNameSynonymModel, blank=True)

    source = models.CharField(max_length=128, blank=True, null=True)
    aired_from = models.DateTimeField(blank=True, null=True)
    aired_to = models.DateTimeField(blank=True, null=True)

    # Image fields
    banner = models.ImageField(
        upload_to=banner_upload_pattern,
        default=None,
        blank=True,
        null=True,
    )
    cover = models.ImageField(
        upload_to=cover_upload_pattern,
        default=None,
        blank=True,
        null=True,
    )
    # Image field nearest color
    banner_background_color = ColorField(null=True, blank=True)
    cover_background_color = ColorField(null=True, blank=True)

    synopsis = models.TextField(blank=True, null=True)
    background = models.TextField(blank=True, null=True)
    rating = models.CharField(blank=True, default="", max_length=50)

    genres = models.ManyToManyField(AnimeGenreModel, blank=True)
    themes = models.ManyToManyField(AnimeThemeModel, blank=True)

    characters = models.ManyToManyField(CharacterModel, blank=True)

    # Producers and studios are the same
    studios = models.ManyToManyField(ProducerModel, blank=True, related_name="studios")
    producers = models.ManyToManyField(ProducerModel, blank=True, related_name="producers")

    staffs = models.ManyToManyField(StaffModel, blank=True)

    recommendations = models.ManyToManyField("self", blank=True)
    episodes = models.ManyToManyField(EpisodeModel, blank=True)

    openings = models.ManyToManyField(AnimeOpeningModel, blank=True)
    endings = models.ManyToManyField(AnimeEndingModel, blank=True)

    comments = models.ManyToManyField(CommentModel, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        indexes = [
            GinIndex(
                fields=["name", "name_japanese"],
                name="anime_name|name_japanese_idx",
                opclasses=["gin_trgm_ops", "gin_trgm_ops"],
            ),
        ]
        verbose_name = "Anime"
