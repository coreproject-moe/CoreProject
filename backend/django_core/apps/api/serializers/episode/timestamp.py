from apps.episodes.models.episode_timestamp import EpisodeTimestampModel
from rest_framework import serializers


class EpisodeTimpstampSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeTimestampModel
        fields = [
            "timestamp",
            "user",
        ]
