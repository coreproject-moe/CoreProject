from ninja import Field, ModelSchema, Schema

from ..models import EpisodeTimestampModel


class EpisodeTimestampTotalTimestampSchema(Schema):
    total_watchtime: int


class EpisodeTimestampGETSchema(ModelSchema):
    user: str | None = Field(..., alias="user.username")

    class Config:
        model = EpisodeTimestampModel
        model_exclude = ["episode", "id"]


class EpisodeTimestampPOSTSchema(ModelSchema):
    class Config:
        model = EpisodeTimestampModel
        model_exclude = ["episode", "id", "user"]
