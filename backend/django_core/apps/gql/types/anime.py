import strawberry
from apps.anime.models import AnimeModel
from strawberry import auto
import strawberry_django
from ..filters.anime import AnimeFilter
import datetime

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
    aired_from: datetime.datetime | None = None
    aired_to: datetime.datetime | None = None

    banner: auto
    cover: auto

    banner_background_color: str
    cover_background_color: str

    synopsis: auto
    background: auto
    rating: auto
