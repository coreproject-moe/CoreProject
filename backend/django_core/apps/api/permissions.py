from django.http import HttpRequest
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.views import APIView


class IsSuperUserOrReadOnly(BasePermission):
    """
    The request is authenticated as a superuser, or is a read-only request.
    """

    def has_permission(self, request: HttpRequest, view: APIView) -> bool:
        return bool(
            request.method in SAFE_METHODS
            or request.user
            and request.user.is_authenticated
            and request.user.is_superuser
        )
