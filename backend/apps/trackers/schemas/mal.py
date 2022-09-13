from ninja import ModelSchema

from ..models import MalModel


class MALGETSchema(ModelSchema):
    class Config:
        model = MalModel
        model_fields = "__all__"


class MALPOSTSchema(ModelSchema):
    class Config:
        model = MalModel
        model_exclude = ["user", "id", "created_at"]
