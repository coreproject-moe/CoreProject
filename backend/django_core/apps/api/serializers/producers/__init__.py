from apps.producers.models import ProducerModel
from rest_framework import serializers


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProducerModel
        fields = [
            "mal_id",
            "kitsu_id",
            "name",
            "name_japanese",
            "established",
            "about",
        ]
