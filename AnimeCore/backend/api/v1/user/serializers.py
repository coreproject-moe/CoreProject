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
            # "user_permissions",
            "date_joined",
            "last_login",
            "is_superuser",
            "is_staff",
            "avatar",
        )
        read_only_fields = [
            "id",
            # "user_permissions",
            "date_joined",
            "last_login",
            "is_superuser",
            "is_staff",
        ]

    def validate_password(self, cleaned_data):
        if cleaned_data == "":
            return ""

        hashed_password = make_password(cleaned_data)
        return hashed_password

    def validate_email(self, cleaned_data):
        # If email exists whats the point of adding another user to it ?
        if get_user_model().objects.filter(email=cleaned_data).exists():
            raise serializers.ValidationError("Email already exists")

        return cleaned_data

    def create(self, validated_data):
        return super().create(validated_data)
