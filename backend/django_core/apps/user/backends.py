import contextlib
from typing import Any, cast

from apps.user.models import CustomUser
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import AbstractBaseUser
from django.db.models import Q
from django.http import HttpRequest


class EmailOrUsernameModelBackend(ModelBackend):
    """
    Authentication backend which allows users to authenticate using either their
    username or email address

    Source: https://stackoverflow.com/a/35836674/59984
    """

    @staticmethod
    def get_user_given_username_and_password(
        username_or_email: str | None,
        password: str | None,
    ) -> CustomUser | None:
        if not username_or_email and not password:
            return None
        query = None

        # Supress user doesn't exist
        with contextlib.suppress(CustomUser.DoesNotExist):
            user_model = CustomUser.objects.get_username_with_discriminator().get(
                Q(username_with_discriminator=username_or_email)
                | Q(email__iexact=username_or_email)
            )

            # If password matches then return user
            if user_model.check_password(password):
                query = user_model

        return query

    def authenticate(
        self,
        request: HttpRequest | None,
        username: str | None = None,
        password: str | None = None,
        **kwargs: Any,
    ) -> AbstractBaseUser | None:
        user_model = self.get_user_given_username_and_password(username, password)
        return cast(AbstractBaseUser, user_model)
