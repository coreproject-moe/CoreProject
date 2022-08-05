from ninja import ModelSchema

from ..models import AnimeCharacterModel


class AnimeCharacterSchema(ModelSchema):
    class Config:
        model = AnimeCharacterModel
        model_fields = "__all__"
