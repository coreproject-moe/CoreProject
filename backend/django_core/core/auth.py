from typing import Self

from apps.user.models import CustomUser, Token
from ninja.security import HttpBearer

from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest


class AuthBearer(HttpBearer):
    def authenticate(
        self: Self,
        request: HttpRequest,
        token: str,
    ) -> CustomUser | AnonymousUser:
        try:
            token_data = Token.objects.get(token=token)
            user: CustomUser = token_data.user

        except Token.DoesNotExist:
            user = AnonymousUser

        finally:
            return user
