from apps.user.models import CustomUser
from strawberry import auto
import strawberry_django
import strawberry


@strawberry_django.type(CustomUser)
class UserType:
    username: auto
    email: auto


