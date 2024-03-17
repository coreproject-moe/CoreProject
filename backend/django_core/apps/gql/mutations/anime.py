import strawberry_django
from strawberry import auto
from apps.anime.models import AnimeModel


@strawberry_django.input(AnimeModel)
class AnimeInput:
    mal_id: auto
    anilist_id: auto
    kitsu_id: auto

    name: auto
    name_japanese: auto
    name_synonyms: list[str]

    source: auto
    aired_from: auto
    aired_to: auto

    synopsis: str | None = None
    background: str | None = None
    rating: str | None = None

    # Images
    banner: auto
    cover: auto

    # We need pk for these
    staffs: list[str] = None
    genres: list[str] = None
    themes: list[str] = None
    studios: list[str] = None
    producers: list[str] = None
    characters: list[str] = None
