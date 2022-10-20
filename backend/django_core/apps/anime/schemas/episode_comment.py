from ninja import Field, ModelSchema

from ..models import EpisodeCommentModel


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
