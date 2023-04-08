from apps.episodes.models.episode_comment import EpisodeCommentModel
from ninja import Field, ModelSchema, Schema
import datetime


class EpisodeCommentGETSchema(ModelSchema):
    user: str | None = Field(..., alias="user.username")

    class Config:
        model = EpisodeCommentModel
        model_fields = ["id", "user", "text"]


class EpisodeCommentTreePOSTSchema(Schema):
    parent_pk: int | None = None
    text: str


class EpisodeCommentTreePATCHSchema(Schema):
    pk: int
    text: str


class EpisodeCommentTreeGETSchema(Schema):
    pk: int
    user: str
    text: str
    comment_added: datetime.datetime
    children: list["EpisodeCommentTreeGETSchema"] = []
