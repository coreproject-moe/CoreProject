from apps.producers.models import ProducerModel
from rest_framework import serializers


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProducerModel
        fields = "__all__"
