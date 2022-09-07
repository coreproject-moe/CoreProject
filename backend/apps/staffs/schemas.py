from ninja import ModelSchema

from .models import StaffModel


class StaffSchema(ModelSchema):
    class Config:
        model = StaffModel
        model_exclude = [
            "id",
        ]
