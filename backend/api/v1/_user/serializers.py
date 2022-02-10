from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "user_permissions",
            "date_joined",
            "last_login",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "user_permissions": {"read_only": True},
            "date_joined": {"read_only": True},
            "last_login": {"read_only": True},
        }
