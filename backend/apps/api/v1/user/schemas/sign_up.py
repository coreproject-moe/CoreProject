from django.contrib.auth import get_user_model
from ninja import ModelSchema


class SignupSchema(ModelSchema):
    class Config:
        model = get_user_model()
        model_exclude = [
            "id",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
            "user_permissions",
            "groups",
        ]
