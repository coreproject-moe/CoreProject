from strawberry_django_plus import gql
from apps.anime.models import AnimeModel


@gql.django.input(AnimeModel)
class AnimeModelInput:
    mal_id: int
    anilist_id: int | None
    kitsu_id: int | None

    name: str
    name_japanese: str | None
    name_synonyms: list[str] | None
