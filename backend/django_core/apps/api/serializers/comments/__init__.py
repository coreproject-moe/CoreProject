from apps.comments.models import CommentModel
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


class CommentSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)
    user = UserSerializer(read_only=True)
    text = serializers.CharField()
    path = serializers.CharField(required=False)
    children = serializers.SerializerMethodField()
    ratio = serializers.IntegerField()

    def get_children(self, obj: CommentModel) -> int:
        if hasattr(obj, "children"):
            return obj.children().count()
