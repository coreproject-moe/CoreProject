from django.contrib.auth import get_user_model
from ninja import ModelSchema


class UserSchema(ModelSchema):
    class Config:
        model = get_user_model()
        model_exclude = [
            "password",
            "ip",  # https://github.com/pydantic/pydantic/issues/333
        ]


# Extra Imports
# __ DO NOT MODIFY __

from .sign_up import SignupSchema
