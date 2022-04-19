from rest_framework import serializers

from ..models import EpisodeModel, EpisodeTimestampModel
from .episode_timestamp import EpisodeTimestampSerializer


class EpisodeSerializer(serializers.ModelSerializer):
    episode_timestamps = EpisodeTimestampSerializer(many=True)
    episode_comments = serializers.SerializerMethodField()

    class Meta:
        model = EpisodeModel
        exclude = ("id",)
        read_only_fields = (
            "episode_number",
            "episode_name",
            "episode_cover",
            "episode_file",
            "episode_summary",
        )

    def get_episode_comments(self, instance):
        return instance.episode_comments.all().count()

    def update(self, instance: EpisodeModel, validated_data) -> dict:
        user = self.context["request"].user

        episode_timestamps = validated_data.get("episode_timestamps", None)
        if episode_timestamps:
            for item in episode_timestamps:
                (
                    timestamp_model,
                    timestamp_model_created,
                ) = EpisodeTimestampModel.objects.update_or_create(
                    user=user,
                    defaults={
                        "episode_number": instance.episode_number,
                        "timestamp": item["timestamp"],
                    },
                )
                timestamp_model.save()

                if timestamp_model_created:
                    instance.episode_timestamps.add(timestamp_model)

        return validated_data

    def to_representation(self, instance):
        serializer = super().to_representation(instance)
        try:
            timestamp_query = instance.episode_timestamps.get(
                user=self.context["request"].user
            )
            serializer["episode_timestamps"] = EpisodeTimestampSerializer(
                timestamp_query,
                many=True,
            ).data

        except instance.episode_timestamps.model.DoesNotExist:
            pass

        finally:
            return serializer
