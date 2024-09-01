from apps.characters.models import CharacterModel
from strawberry import auto
from strawberry.file_uploads import Upload
import strawberry_django


@strawberry_django.input(CharacterModel)
class CharacterInput:
    mal_id: auto
    kitsu_id: auto
    anilist_id: auto

    name: auto
    name_kanji: auto
    character_image: Upload
    about: auto
