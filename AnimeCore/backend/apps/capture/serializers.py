from rest_framework import serializers

from .models import (
    CaptureAnimeNameModel,
    CaptureEpisodeModel,
    CaptureInfoModel,
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


class CaptureInfoSerializer(serializers.ModelSerializer):
    video_timestamps = CaptureAnimeNameSerializer(many=True)

    class Meta:
        model = CaptureInfoModel
        exclude = ("id",)

    def update(self, instance: CaptureInfoModel, validated_data):
        user = validated_data["user"]

        video_volume = validated_data.get("video_volume", None)
        if video_volume:
            instance.video_volume = video_volume

        timestamps = validated_data.get("video_timestamps", None)
        if timestamps:
            for items in timestamps:
                (
                    capture_anime_model,
                    capture_anime_model_created,
                ) = instance.timestamps.update_or_create(
                    anime=items["anime"],
                    user=user,
                )
                if capture_anime_model_created:
                    instance.timestamps.add(capture_anime_model)

                episodes = items["episodes"]

                for episode in episodes:
                    (
                        capture_episode_model,
                        capture_episode_model_created,
                    ) = CaptureEpisodeModel.objects.update_or_create(
                        episode=episode["episode"],
                        user=user,
                        defaults={
                            "timestamp": episode["timestamp"],
                        },
                    )
                    capture_episode_model.save()

                    if capture_episode_model_created:
                        capture_anime_model.episodes.add(capture_episode_model)

        instance.save()
        return validated_data
