import strawberry
from apps.characters.models import CharacterModel

from ..filters.character import CharacterFilter


@strawberry.django.type(CharacterModel, filters=CharacterFilter)
class Character:
    mal_id: int
    kitsu_id: int
    anilist_id: int

    name: str
    name_kanji: str

    character_image: str
    about: str
