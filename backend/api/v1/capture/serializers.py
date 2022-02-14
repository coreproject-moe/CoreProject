from rest_framework import serializers

from .models import CaptureModel


class CaptureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaptureModel
        fields = (
            "video_volume",
            # "user",
        )
