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

    synopsis: auto
    background: auto
    rating: auto

    # Images
    banner: auto
    cover: auto

    # We need pk for these
    staffs: list[int] = None
    genres: list[int] = None
    themes: list[int] = None
    studios: list[int] = None
    producers: list[int] = None
    characters: list[int] = None
