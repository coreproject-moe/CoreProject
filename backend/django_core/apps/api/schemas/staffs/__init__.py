from ninja import ModelSchema

from ....staffs.models import StaffModel, StaffAlternateNameModel


class StaffAlternateNameSchema(ModelSchema):
    class Config:
        model = StaffAlternateNameModel
        model_fields = ["name"]


class StaffSchema(ModelSchema):
    alternate_names: list[StaffAlternateNameSchema] = []

    class Config:
        model = StaffModel
        model_exclude = [
            "id",
        ]
