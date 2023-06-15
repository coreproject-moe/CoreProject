from typing import Any

from django.contrib.auth.models import User
from django.http import HttpRequest

SAFE_METHODS = ("GET", "HEAD", "OPTIONS")


class IsSuperUser:
    def __init__(self, request: HttpRequest, user: User) -> None:
        self.request = request
        self.user = user

    def has_permissions(self, *args: Any, **kwds: Any) -> Any:
        if self.user.is_superuser and self.request.method not in SAFE_METHODS:
            return True
        return False
