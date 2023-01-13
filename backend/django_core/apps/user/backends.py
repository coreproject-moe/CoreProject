from typing import Self

from apps.user.models import CustomUser
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
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
        username_or_email: str, password: str
    ) -> CustomUser:
        query = None
        # So `username` is something like baseplate-admin#0001
        # we need to split to get the username and discriminator
        try:
            user_model: CustomUser = (
                CustomUser.objects.get_username_with_discriminator().get(
                    Q(username_with_discriminator=username_or_email)
                    | Q(email__iexact=username_or_email)
                )
            )
            # If password matches then return user
            if check_password(password, user_model.password):
                query = user_model

        finally:
            return query

    def authenticate(
        self: Self,
        request: HttpRequest | None,
        username: str | None = None,
        password: str | None = None,
    ) -> CustomUser | None:
        return self.get_user_given_username_and_password(username, password)
