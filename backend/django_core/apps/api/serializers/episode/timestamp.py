from apps.episodes.models.episode_timestamp import EpisodeTimestampModel
from rest_framework import serializers


class EpisodeTimpstampSerializer(serializers.Serializer):
    user = serializers.CharField(read_only=True)
    timestamp = serializers.IntegerField()
