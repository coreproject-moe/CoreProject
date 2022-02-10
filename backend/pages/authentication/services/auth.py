from asgiref.sync import sync_to_async

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages

from django.contrib.auth import authenticate

from custom.user.models import CustomUser as User

from django.http.request import HttpRequest


@sync_to_async
def get_user_for_auth(username: str, password: str) -> User:
    return authenticate(username=username, password=password)


@sync_to_async
def auth_login(request: HttpRequest, user: User) -> None:
        login(request, user)


@sync_to_async()
def auth_logout(request: HttpRequest) -> None:
    logout(request)
