from ninja import ModelSchema

from apps.anime.models import AnimeSynonymModel


class AnimeSynonymSchema(ModelSchema):
    class Config:
        model = AnimeSynonymModel
        model_fields = "__all__"
