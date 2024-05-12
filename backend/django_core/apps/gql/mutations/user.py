import strawberry
from strawberry.types import Info
import strawberry_django

from ..types.token import TokenType
from ..models import Token
from ..permissions import IsAuthenticated
from django.contrib.auth import (
    authenticate as django_authenticate,
    login as django_login,
    logout as django_logout,
)
from django.http.request import HttpRequest
from typing import cast


@strawberry.type
class UserMutation:
    @strawberry_django.mutation()
    def login(self, info: Info, username: str, password: str) -> TokenType | None:
        request: HttpRequest = cast(HttpRequest, info.context["request"])
        user = django_authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            token, _ = Token.objects.get_or_create(user=user.pk)
            return token

    @strawberry_django.mutation(permission_classes=[IsAuthenticated])
    def logout(self, info: Info, token: str) -> bool:
        request: HttpRequest = cast(HttpRequest, info.context["request"])
        try:
            token_instance = Token.objects.get(token=token)
            token_instance.delete()
            django_logout(request)
            return True

        except Token.DoesNotExist:
            return False
