from rest_framework import serializers

from ..models import AnimeProducerModel


class AnimeProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeProducerModel
        fields = "__all__"
