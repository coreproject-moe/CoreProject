from rest_framework import serializers

from .models import (
    CaptureTimeStampModel,
    CaptureAnimeNameModel,
    CaptureEpisodeModel,
    CaptureVolumeModel,
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


class CaptureTimeStampSerializer(serializers.ModelSerializer):
    video_timestamps = CaptureAnimeNameSerializer(many=True, required=False)

    class Meta:
        model = CaptureTimeStampModel
        exclude = (
            "id",
            "user",
        )

    def update(self, instance: CaptureTimeStampModel, validated_data):
        user = self.context["user"]  # Dont use get here. Fail if theres nothing.

        timestamps = validated_data.get("video_timestamps", None)
        if timestamps:
            for items in timestamps:
                (
                    capture_anime_model,
                    capture_anime_model_created,
                ) = instance.video_timestamps.get_or_create(
                    anime=items["anime"],
                    user=user,
                )

                if capture_anime_model_created:
                    instance.video_timestamps.add(capture_anime_model)

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


class CaptureVolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaptureVolumeModel
        fields = "__all__"
        read_only_fields = ("user",)
