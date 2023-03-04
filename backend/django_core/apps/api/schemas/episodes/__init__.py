from apps.episodes.models import EpisodeModel
from ninja import ModelSchema


class EpisodeGETSchema(ModelSchema):
    class Config:
        model = EpisodeModel
        model_fields = "__all__"
