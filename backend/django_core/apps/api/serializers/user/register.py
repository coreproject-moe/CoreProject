from rest_framework import serializers
from apps.user.models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser

        exclude = (
            "is_staff",
            "is_active",
            "last_login",
            "is_superuser",
            "groups",
            "created_at",
            "user_permissions",
        )
