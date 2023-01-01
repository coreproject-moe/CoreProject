from apps.anime.models import AnimeSynonymModel
from ninja import ModelSchema


class AnimeSynonymSchema(ModelSchema):
    class Config:
        model = AnimeSynonymModel
        model_fields = "__all__"
