import typing
import strawberry
from strawberry.permission import BasePermission
from strawberry.types import Info
from django.http import HttpRequest

from apps.user.models import CustomUser


class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    # This method can also be async!
    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        user: CustomUser = info.context.get("user", None)
        return True if user else False
