from apps.user.models import CustomUser, Token
from ninja.security import HttpBearer

from django.shortcuts import get_object_or_404


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        token = get_object_or_404(Token, token=token)
        user: CustomUser = token.user
        return user
