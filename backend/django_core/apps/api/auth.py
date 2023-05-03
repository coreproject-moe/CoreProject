import logging
from typing import Any

from apps.user.models import CustomUser
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest
from ninja.compatibility import get_headers
from ninja.security import HttpBearer

from .models import Token

logger = logging.getLogger("django")


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


class OptionalAuthBearer(AuthBearer):
    def __call__(self, request: HttpRequest) -> Any | None:
        headers = get_headers(request)
        auth_value = headers.get(self.header)
        if not auth_value:
            return AnonymousUser()  # if there is no key, we return AnonymousUser object
        parts = auth_value.split(" ")

        if parts[0].lower() != self.openapi_scheme:
            if settings.DEBUG:
                logger.error(f"Unexpected auth - '{auth_value}'")
            return None
        token = " ".join(parts[1:])
        return self.authenticate(request, token)
