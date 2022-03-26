from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.http.request import HttpRequest

from .models import CaptureVolumeModel
from .serializers import CaptureVolumeSerializer

# Create your views here.


class CaptureVolumeView(viewsets.ViewSet, mixins.ListModelMixin):
    """
    AnimeCore (video player)
    ⦿   Player Volume
    """

    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        JWTAuthentication,
        SessionAuthentication,
    ]

    def post(self, request: HttpRequest) -> Response:
        instance, _ = CaptureVolumeModel.objects.get_or_create(user=request.user)
        serializer = CaptureVolumeSerializer(
            data=request.data,
            instance=instance,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
