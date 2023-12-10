from apps.comments.models import CommentModel
from apps.user.models import CustomUser
from django.db.models import Case, Value, When
from django.http import HttpRequest
from rest_framework import serializers
from typing import Literal


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
    pk = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    user = UserSerializer(read_only=True)
    text = serializers.CharField()
    path = serializers.CharField(required=False)
    childrens = serializers.IntegerField(read_only=True)
    ratio = serializers.IntegerField(read_only=True)

    user_reaction = serializers.SerializerMethodField(method_name="get_user_reaction")

    def get_user_reaction(self, obj: CommentModel) -> str | None:
        request: HttpRequest = self.context["request"]
        queryset: dict[
            Literal["ratio"], Literal["upvoted"] | Literal["downvoted"] | None
        ] = (
            CommentModel.objects.annotate(
                ratio=Case(
                    When(upvotes=request.user.pk, then=Value("upvoted")),
                    When(downvotes=request.user.pk, then=Value("downvoted")),
                    default=Value(None),
                )
            )
            .values("ratio")
            .get(pk=obj.pk)
        )

        return queryset["ratio"]
