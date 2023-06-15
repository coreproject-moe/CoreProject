import strawberry
from strawberry import auto

from apps.anime.models import AnimeModel, AnimeNameSynonymModel

__all__ = ["Anime"]


@strawberry.django.type(AnimeNameSynonymModel)
class AnimeNameSynonym:
    name: auto


@strawberry.django.type(AnimeModel, pagination=True)
class Anime:
    id: auto

    mal_id: auto
    anilist_id: auto
    kitsu_id: auto

    # name and name synonym
    name: auto
    name_japanese: auto
    name_synonyms: "AnimeNameSynonym"

    source: auto
    aired_from: auto
    aired_to: auto

    banner: auto
    cover: auto

    banner_background_color: str
    cover_background_color: str

    synopsis: auto
    background: auto
    rating: auto
