from apps.trackers.models import KitsuModel
from ninja import ModelSchema


class KitsuGETSchema(ModelSchema):
    class Config:
        model = KitsuModel
        model_fields = "__all__"


class KitsuPOSTSchema(ModelSchema):
    class Config:
        model = KitsuModel
        model_exclude = ["user", "id", "created_at"]
