import strawberry
from apps.anime.models.anime_theme import AnimeThemeModel


@strawberry.django.filters.filter(AnimeThemeModel, lookups=True)
class AnimeThemeFilter:
    mal_id: int
    name: str
    type: str
