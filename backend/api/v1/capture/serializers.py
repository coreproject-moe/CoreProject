from rest_framework import serializers

from api.v1._user.serializers import UserSerializer
from .models import CaptureModel


class CaptureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaptureModel
        fields = (
            "video_volume",
            # "user",
        )
