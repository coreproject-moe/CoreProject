from ninja import ModelSchema

from ....staffs.models import StaffAlternateNameModel, StaffModel


class StaffAlternateNameSchema(ModelSchema):
    class Config:
        model = StaffAlternateNameModel
        model_fields = ["name"]


class StaffGETSchema(ModelSchema):
    alternate_names: list[StaffAlternateNameSchema] = []

    class Config:
        model = StaffModel
        model_fields = "__all__"


class StaffPOSTSchema(ModelSchema):
    alternate_names: list[StaffAlternateNameSchema] = []

    class Config:
        model = StaffModel
        model_exclude = [
            "id",
            "created_at",
            "updated_at",
            "is_locked",
        ]
