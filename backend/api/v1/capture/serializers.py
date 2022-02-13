from rest_framework import serializers

from .._user.serializers import UserSerializer
from .models import CaptureModel


class CaptureSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)

    class Meta:
        model = CaptureModel
        fields = (
            "video_volume",
            "user",
        )
