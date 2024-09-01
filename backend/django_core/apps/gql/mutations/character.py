import strawberry
from strawberry import Info
import strawberry_django
from ..types.character import CharacterType
from ..permissions import IsSuperUser
from ..input.character import CharacterInput


@strawberry.type
class CharacterMutation:
    @strawberry_django.mutation(
        permission_classes=[IsSuperUser],
        extensions=[strawberry_django.permissions.IsSuperuser()],
    )
    def add_character(self, info: Info, data: CharacterInput) -> CharacterType:
        pass
