from ninja import ModelSchema

from ..models import KitsuModel


class KitsuGETSchema(ModelSchema):
    class Config:
        model = KitsuModel
        model_fields = "__all__"


class KitsuPOSTSchema(ModelSchema):
    class Config:
        model = KitsuModel
        model_exclude = ["user", "id", "created_at"]
