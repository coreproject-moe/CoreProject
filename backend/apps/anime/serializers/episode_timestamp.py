from rest_framework import serializers
from ..models import EpisodeTimestampModel

class EpisodeTimestampSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeTimestampModel
        exclude = (
            "id",
            "episode_number",
        )
