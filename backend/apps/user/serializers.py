from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "user_permissions",
            "date_joined",
            "last_login",
            "is_superuser",
            "is_staff",
            "avatar",
            "video_volume",
        )
        read_only_fields = [
            "id",
            "user_permissions",
            "date_joined",
            "last_login",
            "is_superuser",
            "is_staff",
            "email",
        ]
        extra_kwargs = {
            "password": {
                "required": False,
                "write_only": True,
            },
            "username": {
                "required": False,
            },
            "email": {
                "required": False,
            },
        }

    def validate_email(self, cleaned_data):
        # If email exists whats the point of adding another user to it ?
        if get_user_model().objects.filter(email=cleaned_data).exists():
            raise serializers.ValidationError("Email already exists")

        return cleaned_data

    def validate(self, cleaned_data):
        password = cleaned_data.get("password", None)

        if password:
            hashed_password = make_password(password)
            cleaned_data["password"] = hashed_password
        else:
            cleaned_data.pop("password", None)

        return cleaned_data
