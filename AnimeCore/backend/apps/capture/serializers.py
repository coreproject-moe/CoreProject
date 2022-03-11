from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from apps.upload.models import AnimeInfoModel, EpisodeModel

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
    episodes = CaptureEpisodeSerializer(many=True)

    class Meta:
        model = CaptureAnimeNameModel
        exclude = ("id", "user")


class CaptureVideoSerializer(serializers.ModelSerializer):
    timestamps = CaptureAnimeNameSerializer(many=True)
    user = serializers.CharField(source="user.username")

    class Meta:
        model = CaptureVideoModel
        fields = "__all__"

    def update(self, instance: CaptureVideoModel, validated_data):
        user = validated_data["user"]["username"]
        if not user:
            return

        video_volume = validated_data.get("video_volume", None)
        anime_name = (
            validated_data.get("timestamps", None)[0]
            .get("anime", None)
            .get("anime_name", None)
        )

        episodes = validated_data.get("timestamps", None)[0].get("episodes", None)

        if anime_name:
            try:
                capture_anime_model = instance.timestamps.get(
                    anime__anime_name__exact=anime_name, user__username__exact=user
                )

            except ObjectDoesNotExist:
                capture_anime_model = CaptureAnimeNameModel.objects.create(
                    anime=AnimeInfoModel.objects.get(anime_name=anime_name),
                    user=get_user_model().objects.get(username=user),
                )
                instance.timestamps.add(capture_anime_model)

            finally:
                for i in episodes:
                    try:
                        capture_episode_model = capture_anime_model.episodes.get(
                            episode__episode_name__exact=i.get("episode").get(
                                "episode_name"
                            )
                        )
                        capture_episode_model.timestamp = i.get("timestamp")
                        capture_episode_model.save()

                    except ObjectDoesNotExist:
                        capture_episode_model = CaptureEpisodeModel.objects.create(
                            episode=EpisodeModel.objects.get(
                                episode_name=i.get("episode").get("episode_name"),
                            ),
                            timestamp=i.get("timestamp"),
                            user=get_user_model().objects.get(username=user),
                        )
                        # Save it so we can add it to episode list.
                        capture_episode_model.save()
                        capture_anime_model.episodes.add(capture_episode_model)

        if video_volume:
            instance.video_volume = video_volume

        instance.save()
        return validated_data
