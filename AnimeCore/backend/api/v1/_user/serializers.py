from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False, write_only=True)

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
            "avatar",
        )
        read_only_fields = [
            "id",
            "username",
            "email",
            "user_permissions",
            "date_joined",
            "last_login",
        ]

    def validate(self, cleaned_data):
        password: str = cleaned_data.get("password", None)

        if password:
            hashed_password = make_password(password)
            cleaned_data["password"] = hashed_password
        else:
            cleaned_data.pop("password",None)

        return cleaned_data
