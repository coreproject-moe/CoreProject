import sys
from functools import wraps
from django.http import HttpRequest
from typing import Optional, TYPE_CHECKING
from django.contrib.auth.models import AnonymousUser
from http import HTTPStatus
from ninja.errors import HttpError

if TYPE_CHECKING:
    from .permissions import IsSuperUser


def recursionlimit(limit):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            old_limit = sys.getrecursionlimit()
            sys.setrecursionlimit(limit)
            try:
                result = func(*args, **kwargs)
            finally:
                sys.setrecursionlimit(old_limit)
            return result

        return wrapper

    return decorator


def throttle():
    def decorator(func):
        @wraps(func)
        def wrapper(request: HttpRequest, *args, **kwargs):
            path = request.path
            if False:
                return 429, None
            return func(request, *args, **kwargs)

        return wrapper

    return decorator


def permission_required(permissions: list["IsSuperUser"], key: Optional[str] = "auth"):
    def decorator(func):
        @wraps(func)
        def wrapper(request: HttpRequest, *args, **kwargs):
            try:
                user = getattr(request, key)
            except AttributeError:
                user = AnonymousUser

            permission_granted = any(
                [permission(request, user).has_permissions() for permission in permissions]
            )
            if not permission_granted:
                raise HttpError(
                    HTTPStatus.UNAUTHORIZED,
                    "Superuser is required for this operation",
                )
            return func(request, *args, **kwargs)

        return wrapper

    return decorator
