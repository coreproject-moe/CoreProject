from ninja import ModelSchema

from ..models import EpisodeModel


class EpisodeGETSchema(ModelSchema):
    class Config:
        model = EpisodeModel
        model_fields = "__all__"


class EpisodePOSTSchema(ModelSchema):
    class Config:
        model = EpisodeModel
        model_exclude = [
            "episode_comments",
            "episode_timestamps",
        ]
