from ninja.security import HttpBasicAuth
from django.contrib.auth import get_user_model
from apps.user.models import CustomUser
from django.db.models import Q
from django.contrib.auth.hashers import check_password


class AuthBearer(HttpBasicAuth):
    def authenticate(self, request, username: str, password: str) -> str:
        try:
            user_model: CustomUser = (
                CustomUser.objects.get_username_with_discriminator().get(
                    Q(username_with_discriminator=username) | Q(email__iexact=username)
                )
            )
            if check_password(password, user_model.password):
                query = user_model

        except CustomUser.DoesNotExist:
            query = None

        finally:
            return query
