from ninja import ModelSchema

from .models import CharacterModel


class CharacterSchema(ModelSchema):
    class Config:
        model = CharacterModel
        model_exclude = [
            "id",
        ]
