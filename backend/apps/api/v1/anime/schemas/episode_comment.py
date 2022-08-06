from ..models import EpisodeCommentModel
from ninja import ModelSchema, Field


class EpisodeCommentGETSchema(ModelSchema):
    user: str | None = Field(..., alias="user.username")

    class Config:
        model = EpisodeCommentModel
        model_fields = "__all__"
