import strawberry
from apps.anime.models.anime_genre import AnimeGenreModel


@strawberry.django.filters.filter(AnimeGenreModel, lookups=True)
class AnimeGenreFilter:
    mal_id: int
    name: str
    type: str
