from ..models import EpisodeTimestampModel
from ninja import ModelSchema, Field


class EpisodeTimestampGETSchema(ModelSchema):
    user: str | None = Field(..., alias="user.username")

    class Config:
        model = EpisodeTimestampModel
        model_exclude = ["episode", "id"]


class EpisodeTimestampPOSTSchema(ModelSchema):
    class Config:
        model = EpisodeTimestampModel
        model_exclude = ["episode", "id", "user"]
