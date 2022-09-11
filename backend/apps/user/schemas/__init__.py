from django.contrib.auth import get_user_model
from ninja import ModelSchema
from pydantic import AnyUrl
from django.shortcuts import resolve_url
from django.conf import settings

from ..models import CustomUser


class UserSchema(ModelSchema):
    avatar: AnyUrl

    class Config:
        model = get_user_model()
        model_exclude = [
            "password",
            "avatar",
            "ip",  # https://github.com/pydantic/pydantic/issues/333
        ]

    @staticmethod
    def resolve_anime_genres(obj: CustomUser) -> str:
        url = resolve_url("avatar-view", user_id=obj.pk)
        return f"{settings.HOSTNAME}{url}"


# Extra Imports
# __ DO NOT MODIFY __

from .sign_up import SignupSchema
