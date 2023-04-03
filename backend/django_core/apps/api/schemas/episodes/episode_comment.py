from apps.episodes.models.episode_comment import EpisodeCommentModel
from ninja import Field, ModelSchema, Schema


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


class EpisodeCommentTreeSchema(Schema):
    node: EpisodeCommentGETSchema
    tree: list["EpisodeCommentTreeSchema"] | None = None
