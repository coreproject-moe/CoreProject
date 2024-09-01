import strawberry_django
from apps.characters.models import CharacterModel


@strawberry_django.input(CharacterModel)
class CharacterInput:
    pass
