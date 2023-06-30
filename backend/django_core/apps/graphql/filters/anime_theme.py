from apps.anime.models.anime_theme import AnimeThemeModel
import strawberry
from strawberry_django.filters import FilterLookup


@strawberry.django.filters.filter(AnimeThemeModel, lookups=True)
class AnimeThemeFilter:
    mal_id: int
    name: str
    type: str
