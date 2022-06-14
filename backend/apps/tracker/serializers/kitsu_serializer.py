from rest_framework import serializers

from ..models import KitsuModel


class KitsuSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitsuModel
        fields = "__all__"
