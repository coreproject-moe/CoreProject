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
