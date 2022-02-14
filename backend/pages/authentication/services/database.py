from django.db.models.base import Model
from django.contrib.auth import get_user_model

from asgiref.sync import sync_to_async

from ..models import PasswordResetUrl
from typing import Optional, Type


@sync_to_async
def get_password_reset_url_database(user_id: int) -> PasswordResetUrl:
    return PasswordResetUrl.objects.get(user=user_id)


@sync_to_async
def get_user_by_id(user_id: int) -> Type[Model]:
    return get_user_model().objects.get(id=user_id)


@sync_to_async()
def check_if_username_exist(username: str) -> bool:
    return get_user_model().objects.filter(username=username).exists()


@sync_to_async()
def check_if_email_exist(email: str) -> bool:
    return get_user_model().objects.filter(email=email).exists()


@sync_to_async
def create_new_user(
    username: str,
    email: str,
    password: str,
    avatar,
    first_name=Optional[str],
    last_name=Optional[str],
) -> None:
    database = get_user_model().objects.create_user(
        username,
        email,
        password,
    )
    if avatar:
        database.avatar = avatar

    database.first_name = first_name
    database.last_name = last_name
    database.save()


@sync_to_async
def create_new_reset_database(user) -> PasswordResetUrl:
    database = PasswordResetUrl(user=user)
    database.save()
    return database
