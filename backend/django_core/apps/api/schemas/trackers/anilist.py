from ninja import ModelSchema

from apps.trackers.models import AnilistModel


class AnilistGETSchema(ModelSchema):
    class Config:
        model = AnilistModel
        model_fields = "__all__"


class AnilistPOSTSchema(ModelSchema):
    class Config:
        model = AnilistModel
        model_exclude = ["user", "id", "created_at"]
