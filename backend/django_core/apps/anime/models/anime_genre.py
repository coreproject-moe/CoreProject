from django.db import models
from mixins.models.created_at import CreatedAtMixin
from mixins.models.is_locked import IsLockedMixin
from mixins.models.updated_at import UpdatedAtMixin

# Create your models here.

TYPE_CHOICES = [
    ("Anime", "anime"),
    ("Manga", "manga"),
]


class AnimeGenreModel(UpdatedAtMixin, CreatedAtMixin, IsLockedMixin):
    mal_id = models.IntegerField(unique=True, blank=False, null=False)
    name = models.CharField(unique=True, max_length=50, default="", null=False, blank=False)
    type = models.CharField(
        max_length=50, choices=TYPE_CHOICES, default="", null=False, blank=False
    )
    description = models.TextField(null=True, blank=False)

    def __str__(self) -> str:
        return f"{self.pk}. {self.name} ({self.type})"

    class Meta:
        verbose_name = "Anime Genre"
