from rest_framework import serializers

from .models import (
    CaptureVolumeModel,
)


class CaptureVolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaptureVolumeModel
        fields = "__all__"
        read_only_fields = ("user",)
