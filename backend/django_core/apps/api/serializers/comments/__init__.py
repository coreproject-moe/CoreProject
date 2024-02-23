from typing import Literal

from apps.comments.models import CommentModel
from apps.user.models import CustomUser
from django.db.models import Case, Value, When
from django.http import HttpRequest
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError


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

    deleted = serializers.BooleanField(read_only=True)
    user_reaction = serializers.SerializerMethodField(method_name="get_user_reaction")

    def get_user_reaction(self, obj: CommentModel) -> str | None:
        request: HttpRequest = self.context["request"]
        queryset: dict[
            Literal["ratio"], Literal["upvoted"] | Literal["downvoted"] | None
        ] = (
            CommentModel.objects.annotate(
                ratio=Case(
                    When(upvotes__in=[request.user.pk], then=Value("upvoted")),
                    When(downvotes__in=[request.user.pk], then=Value("downvoted")),
                    default=Value(None),
                )
            )
            .values("ratio")
            .get(pk=obj.pk)
        )
        return queryset["ratio"]

    def create(self, validated_data):
        serializer_data = {
            "user": self.context["request"].user,
            "text": validated_data["text"],
        }
        if path := validated_data.get("path"):
            anime_comment_model_instance = get_object_or_404(CommentModel, path__match=path)
            comment_instance: "CommentModel" = CommentModel.objects.create_child(
                parent=anime_comment_model_instance, **serializer_data
            )
        else:
            comment_instance: "CommentModel" = CommentModel.objects.create_child(
                **serializer_data
            )
        comment_instance.save()

        return comment_instance

    def update(self, instance: CommentModel, validated_data) -> CommentModel:
        if instance.user != self.context["request"].user:
            raise ValidationError("`user` and instance `user` are different")

        # Only texts can be updated
        instance.text = validated_data["text"]

        instance.save()
        return instance
