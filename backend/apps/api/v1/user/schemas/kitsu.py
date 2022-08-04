from apps.__user__.models import KitsuModel
from ninja import ModelSchema


class KitsuSchema(ModelSchema):
    class Config:
        model = KitsuModel
        model_fields = "__all__"
