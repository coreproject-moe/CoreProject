import typing

from apps.user.models import CustomUser
from strawberry.permission import BasePermission
from strawberry.types import Info


class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    # This method can also be async!
    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        user: CustomUser = info.context.get("user", None)
        return True if user.is_authenticated else False


class IsSuperUser(BasePermission):
    message = "User is not superuser"

    # This method can also be async!
    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        user: CustomUser = info.context.get("user", None)
        return True if user.is_authenticated and user.is_superuser else False
