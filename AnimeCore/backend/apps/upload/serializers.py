from rest_framework import serializers

from .models import AnimeInfoModel, EpisodeCommentModel, EpisodeModel


class EpisodeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeCommentModel
        exclude = ("id",)


class EpisodeSerializer(serializers.ModelSerializer):
    episode_comments = EpisodeCommentSerializer(many=True)

    class Meta:
        model = EpisodeModel
        exclude = ("id",)


class AnimeInfoSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True)

    class Meta:
        model = AnimeInfoModel
        exclude = ("id",)

    def update(self, instance: AnimeInfoModel, validated_data):
        print(validated_data)
