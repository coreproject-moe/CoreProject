from apps.anime.models.anime_comment import AnimeCommentModel
from apps.user.models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "avatar",
            "avatar_url",
            "email",
        ]


class AnimeCommentSerializer(serializers.Serializer):
    created_at = serializers.DateTimeField(read_only=True)
    user = UserSerializer(read_only=True)
    text = serializers.CharField()
    path = serializers.CharField(required=False)
    children = serializers.SerializerMethodField()

    def get_children(self, obj: AnimeCommentModel) -> int:
        return obj.children().count()
