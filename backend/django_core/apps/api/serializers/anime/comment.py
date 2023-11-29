from rest_framework import serializers
from apps.user.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "avatar",
            "avatar_provider",
        ]


class AnimeCommentSerializer(serializers.Serializer):
    created_at = serializers.DateTimeField(read_only=True)
    user = UserSerializer(read_only=True)
    text = serializers.CharField()
    path = serializers.CharField(required=False)
