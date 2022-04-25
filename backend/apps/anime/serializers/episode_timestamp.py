from rest_framework import serializers
from ..models import EpisodeTimestampModel, AnimeInfoModel


class EpisodeTimestampSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    episode_number = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = EpisodeTimestampModel
        fields = "__all__"

    def create(self, validated_data):
        data, created = EpisodeTimestampModel.objects.update_or_create(
            episode_number=validated_data["episode_number"],
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
