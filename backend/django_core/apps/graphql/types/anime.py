from apps.anime.models import AnimeModel, AnimeNameSynonymModel
from strawberry import auto
import strawberry_django
from ..filters.anime import AnimeFilter

__all__ = ["Anime"]


@strawberry_django.type(AnimeModel, filters=AnimeFilter)
class Anime:
    id: int

    mal_id: auto
    anilist_id: auto
    kitsu_id: auto

    # name and name synonym
    name: auto
    name_japanese: auto

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
