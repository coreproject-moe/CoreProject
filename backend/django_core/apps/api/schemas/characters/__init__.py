from ninja import ModelSchema

from ....characters.models import CharacterModel


class CharacterGETSchema(ModelSchema):
    class Config:
        model = CharacterModel
        model_fields = "__all__"


class CharacterPOSTSchema(ModelSchema):
    class Config:
        model = CharacterModel
        model_exclude = [
            "id",
            "created_at",
            "updated_at",
            "is_locked",
        ]
