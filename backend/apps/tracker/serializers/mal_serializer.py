from rest_framework import serializers

from ..models import MalModel


class MalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MalModel
        fields = "__all__"
