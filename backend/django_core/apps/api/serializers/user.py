from apps.user.models import CustomUser
from rest_framework import serializers
from django.urls import reverse_lazy


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {
            "password": {
                "write_only": True,
            },
            "is_staff": {
                "read_only": True,
            },
            "is_active": {
                "read_only": True,
            },
            "is_superuser": {
                "read_only": True,
            },
            "date_joined": {
                "read_only": True,
            },
            "last_login": {
                "read_only": True,
            },
            "user_permissions": {
                "read_only": True,
            },
            "groups": {
                "read_only": True,
            },
        }

    def to_representation(self, instance: CustomUser):
        ret = super().to_representation(instance)
        ret["avatar"] = reverse_lazy("avatar_view", args=[instance.pk])
        return ret
