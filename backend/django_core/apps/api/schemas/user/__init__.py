from apps.user.models import CustomUser
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from ninja import ModelSchema


class UserSchema(ModelSchema):
    avatar: str

    class Config:
        model = get_user_model()
        model_exclude = [
            "password",
            "avatar",
        ]

    @staticmethod
    def resolve_avatar(obj: CustomUser) -> str:
        url = reverse_lazy(
            "avatar_view",
            kwargs={
                "user_id": obj.id,
            },
        )
        return f"{url}"
