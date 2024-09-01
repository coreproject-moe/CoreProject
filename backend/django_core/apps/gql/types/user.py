from apps.user.models import CustomUser
from strawberry import auto
import strawberry_django


@strawberry_django.type(CustomUser)
class UserType:
    username: auto
    email: auto
    first_name: auto
    last_name: auto

    is_staff: auto
    is_active: auto
    avatar: auto
    avatar_provider: auto
