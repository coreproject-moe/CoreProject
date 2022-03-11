from rest_framework import serializers

from .models import CaptureVideoVolumeModel


class CaptureVideoVolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaptureVideoVolumeModel
        fields = (
            "video_volume",
            # "user",
        )
