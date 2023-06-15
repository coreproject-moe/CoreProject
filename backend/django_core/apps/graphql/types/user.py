import strawberry
from strawberry import auto
from apps.user.models import CustomUser


@strawberry.django.type(CustomUser)
class User:
    username: auto
    email: auto


@strawberry.django.type(CustomUser)
class UserInput:
    username: auto
    password: auto
