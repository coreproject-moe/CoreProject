import strawberry
from strawberry import auto

from apps.anime.models import AnimeModel


@strawberry.django.type(AnimeModel)
class Anime:
    id: auto

    mal_id: auto
    anilist_id: auto
    kitsu_id: auto
