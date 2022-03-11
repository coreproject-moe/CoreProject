from rest_framework import serializers

from .models import (
    CaptureAnimeNameModel,
    CaptureEpisodeModel,
    CaptureVideoModel,
)


class CaptureEpisodeSerializer(serializers.ModelSerializer):
    episode = serializers.CharField(source="episode.episode_name")

    class Meta:
        model = CaptureEpisodeModel
        exclude = ("id", "user")


class CaptureAnimeNameSerializer(serializers.ModelSerializer):
    anime = serializers.CharField(source="anime.anime_name")
    episdoes = CaptureEpisodeSerializer(many=True)

    class Meta:
        model = CaptureAnimeNameModel
        exclude = ("id", "user")


class CaptureVideoSerializer(serializers.ModelSerializer):
    timestamp = CaptureAnimeNameSerializer(many=True)
    user = serializers.CharField(source="user.username")

    class Meta:
        model = CaptureVideoModel
        fields = "__all__"
