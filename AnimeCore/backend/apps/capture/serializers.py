from rest_framework import serializers

from .models import CaptureVideoVolumeModel, CaptureVideoTimeStampModel


class CaptureVideoVolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaptureVideoVolumeModel
        fields = (
            "video_volume",
            # "user",
        )


class CaptureVideoTimeStampSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaptureVideoTimeStampModel
        fields = ("video_timestamp",)
