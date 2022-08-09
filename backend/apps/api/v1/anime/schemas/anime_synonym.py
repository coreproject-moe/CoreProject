from ninja import ModelSchema

from ..models import AnimeSynonymModel


class AnimeSynonymSchema(ModelSchema):
    class Config:
        model = AnimeSynonymModel
        model_fields = "__all__"
