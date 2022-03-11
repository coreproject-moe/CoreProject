from rest_framework import serializers

from .models import AnimeInfoModel, EpisodeModel


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeModel
        fields = "__all__"


class AnimeInfoSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True)

    class Meta:
        model = AnimeInfoModel
        fields = "__all__"
