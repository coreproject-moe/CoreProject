from rest_framework import serializers

from .models import (
    CaptureAnimeNameModel,
    CaptureEpisodeModel,
    CaptureVideoModel,
)


class CaptureEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaptureEpisodeModel
        exclude = ("id", "user")


class CaptureAnimeNameSerializer(serializers.ModelSerializer):
    episodes = CaptureEpisodeSerializer(many=True)

    class Meta:
        model = CaptureAnimeNameModel
        exclude = ("id", "user")


class CaptureVideoSerializer(serializers.ModelSerializer):
    timestamps = CaptureAnimeNameSerializer(many=True)

    class Meta:
        model = CaptureVideoModel
        fields = "__all__"

    def update(self, instance: CaptureVideoModel, validated_data):
        user = validated_data["user"]
        if not user:
            return

        video_volume = validated_data.get("video_volume", None)
        if video_volume:
            instance.video_volume = video_volume

        timestamps = validated_data.get("timestamps", None)
        for anime in timestamps:
            anime_id = anime["anime"]

            if anime_id:
                (
                    capture_anime_model,
                    capture_anime_model_created,
                ) = instance.timestamps.update_or_create(
                    anime=anime_id,
                    user=user,
                )
                if capture_anime_model_created:
                    instance.timestamps.add(capture_anime_model)

                episodes = anime["episodes"]

                for episode in episodes:
                    (
                        capture_episode_model,
                        capture_episode_model_created,
                    ) = CaptureEpisodeModel.objects.update_or_create(
                        episode=episode["episode"],
                        timestamp=episode["timestamp"],
                        user=user,
                    )
                    capture_episode_model.save()

                    if capture_episode_model_created:
                        capture_anime_model.episodes.add(capture_episode_model)

        instance.save()
        return validated_data
