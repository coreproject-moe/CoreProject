from typing import cast

from apps.characters.models import CharacterModel
from apps.gql.functions.dictionary import clean_dictionary
import strawberry
from strawberry import Info
import strawberry_django

from ..input.character import CharacterInput
from ..permissions import IsSuperUser
from ..types.character import CharacterType


@strawberry.type
class CharacterMutation:
    @strawberry_django.mutation(
        permission_classes=[IsSuperUser],
        extensions=[strawberry_django.permissions.IsSuperuser()],
    )
    def add_character(self, info: Info, data: CharacterInput) -> CharacterType:
        kwargs = {
            "mal_id": data.mal_id,
            "kitsu_id": data.kitsu_id,
            "anilist_id": data.anilist_id,
            "name": data.name,
            "name_kanji": data.name_kanji,
            "character_image": data.character_image,
            "about": data.about,
        }
        model_data = clean_dictionary(dictionary=kwargs)

        instance = CharacterModel.objects.create(**model_data)
        return cast(CharacterType, instance)
