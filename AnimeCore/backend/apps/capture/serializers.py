from rest_framework import serializers

from .models import CaptureVideoModel


class CaptureVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaptureVideoModel
        fields = (
            "video_volume",
            "video_timestamp"
            # "user",
        )
