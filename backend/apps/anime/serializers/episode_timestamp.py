from rest_framework import serializers

from ..models import AnimeInfoModel
from ..models import EpisodeModel
from ..models import EpisodeTimestampModel


class EpisodeTimestampSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = EpisodeTimestampModel
        exclude = ("episode",)

    def create(self, validated_data):
        data, created = EpisodeTimestampModel.objects.update_or_create(
            episode=EpisodeModel.objects.get(
                episode_number=self.context["episode_number"]
            ),
            user=validated_data["user"],
            defaults={
                "timestamp": validated_data["timestamp"],
            },
        )

        if created:
            AnimeInfoModel.objects.get(pk=self.context["anime_id"]).anime_episodes.get(
                episode_number=self.context["episode_number"]
            ).episode_timestamps.add(data)

        return data
