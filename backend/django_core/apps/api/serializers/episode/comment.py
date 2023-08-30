from rest_framework import serializers
from apps.episodes.models import EpisodeCommentModel

import uuid


class EpisodeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeCommentModel
        fields = [
            "user",
            "text",
            "path",
        ]
        extra_kwargs = {
            "path": {
                "required": False,
            }
        }


# class EpisodeCommentPOSTSerializer(serializers.ModelSerializer):
#     class Meta(EpisodeCommentBaseSerializer.Meta):
#         fields = [
#             "user",
#             "text",
#             "path",
#         ]
