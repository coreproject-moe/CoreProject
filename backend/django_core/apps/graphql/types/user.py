import strawberry
from apps.user.models import CustomUser
from strawberry import auto


@strawberry.django.type(CustomUser)
class User:
    username: auto
    email: auto


@strawberry.django.type(CustomUser)
class UserInput:
    username: auto
    password: auto
