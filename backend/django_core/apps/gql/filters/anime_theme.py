import strawberry_django
from apps.anime.models.anime_theme import AnimeThemeModel


@strawberry_django.filters.filter(AnimeThemeModel, lookups=True)
class AnimeThemeFilter:
    mal_id: int | None
    name: str | None
    type: str | None
