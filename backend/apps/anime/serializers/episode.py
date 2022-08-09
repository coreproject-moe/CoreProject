from rest_framework import serializers

from ..models import EpisodeModel


class EpisodeSerializer(serializers.ModelSerializer):
    episode_timestamps = serializers.SerializerMethodField()
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

    def get_episode_timestamps(self, instance):
        return instance.episode_timestamps.all().count()
