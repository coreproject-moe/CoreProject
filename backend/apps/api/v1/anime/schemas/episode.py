from ninja import ModelSchema

from ..models import EpisodeModel


class EpisodeSchema(ModelSchema):
    class Config:
        model = EpisodeModel
        model_fields = "__all__"
