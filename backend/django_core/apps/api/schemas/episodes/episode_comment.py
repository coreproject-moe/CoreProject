from apps.episodes.models.episode_comment import EpisodeCommentModel
from ninja import Field, ModelSchema


class EpisodeCommentGETSchema(ModelSchema):
    user: str | None = Field(..., alias="user.username")

    class Config:
        model = EpisodeCommentModel
        model_fields = "__all__"


class EpisodeCommentPOSTSchema(ModelSchema):
    class Config:
        model = EpisodeCommentModel
        model_fields = [
            "text",
        ]
