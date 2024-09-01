import strawberry_django
from apps.characters.models import CharacterModel

from ..filters.character import CharacterFilter


@strawberry_django.type(CharacterModel, filters=CharacterFilter)
class CharacterType:
    mal_id: int
    kitsu_id: int
    anilist_id: int

    name: str
    name_kanji: str

    character_image: str
    about: str
