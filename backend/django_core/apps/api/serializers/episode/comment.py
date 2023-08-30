from rest_framework import serializers
from apps.episodes.models import EpisodeCommentModel


class EpisodeCommentBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeCommentModel


class EpisodeCommentGETSerializer(EpisodeCommentBaseSerializer):
    class Meta(EpisodeCommentBaseSerializer.Meta):
        fields = [
            "user",
            "text",
            "path",
        ]


class EpisodeCommentPOSTSerializer(serializers.ModelSerializer):
    class Meta(EpisodeCommentBaseSerializer.Meta):
        fields = [
            "user",
            "text",
            "path",
        ]
