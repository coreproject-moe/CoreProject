from apps.episodes.models import EpisodeModel
from rest_framework import serializers


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeModel
        fields = "__all__"
