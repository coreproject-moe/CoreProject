from apps.user.models import CustomUser
from ninja.security import HttpBearer

from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest

from .models import Token


class AuthBearer(HttpBearer):
    def authenticate(
        self,
        request: HttpRequest,
        token: str,
    ) -> CustomUser | AnonymousUser:
        try:
            token_data = Token.objects.get(token=token)
            return token_data.user

        except Token.DoesNotExist:
            return AnonymousUser
