from rest_framework import serializers
from ..models import EpisodeCommentModel


class EpisodeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeCommentModel
        exclude = ("id",)
