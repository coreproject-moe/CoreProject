from django.contrib.auth import get_user_model
from ninja import ModelSchema


class UserSchema(ModelSchema):
    class Config:
        model = get_user_model()
        model_exclude = ["password"]


# Extra Imports
# __ DO NOT MODIFY __

from .signup import SignupSchema
