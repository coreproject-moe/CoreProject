from apps.episodes.models import EpisodeModel
from rest_framework import serializers


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeModel
        fields = [
            "episode_number",
            "episode_name",
            "episode_thumbnail",
            "episode_summary",
            "episode_length",
            "episode_type",
            "providers",
        ]
        extra_kwargs = {
            "created_at": {
                "read_only": True,
            },
            "updated_at": {
                "read_only": True,
            },
        }
