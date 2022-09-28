from apps.user.models import CustomUser


def is_superuser(user: CustomUser) -> bool:
    return all([user.is_active, user.is_superuser])
