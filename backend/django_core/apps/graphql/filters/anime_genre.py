from apps.anime.models.anime_genre import AnimeGenreModel
import strawberry
from strawberry_django.filters import FilterLookup


@strawberry.django.filters.filter(AnimeGenreModel, lookups=True)
class AnimeGenreFilter:
    mal_id: int
    name: str
    type: str
