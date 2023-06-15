import strawberry
from apps.anime.models import AnimeModel
from strawberry import auto


@strawberry.django.type(AnimeModel)
class Anime:
    id: auto

    mal_id: auto
    anilist_id: auto
    kitsu_id: auto
