from strawberry import auto
import strawberry_django
from apps.user.models import CustomUser


@strawberry_django.input(CustomUser)
class UserLoginInput:
    username: auto
    password: auto
