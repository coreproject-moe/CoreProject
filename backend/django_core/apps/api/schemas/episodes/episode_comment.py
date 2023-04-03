from apps.episodes.models.episode_comment import EpisodeCommentModel
from ninja import Field, ModelSchema, Schema
import datetime


class EpisodeCommentGETSchema(ModelSchema):
    user: str | None = Field(..., alias="user.username")

    class Config:
        model = EpisodeCommentModel
        model_fields = ["user", "text", "comment_added"]


class EpisodeCommentPOSTSchema(ModelSchema):
    class Config:
        model = EpisodeCommentModel
        model_fields = [
            "text",
        ]


class EpisodeCommentTreeChildrenSchema(EpisodeCommentGETSchema):
    childrens: list["EpisodeCommentTreeChildrenSchema"] | None = None


class EpisodeCommentTreeSchema(Schema):
    user: str
    text: str
    comment_added: datetime.datetime
    childrens: list["EpisodeCommentTreeChildrenSchema"] | None = None
