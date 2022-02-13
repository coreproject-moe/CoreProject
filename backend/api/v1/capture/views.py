from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.parsers import JSONParser

from .models import CaptureModel
from .serializers import CaptureSerializer
from django.http.response import HttpResponse

# Create your views here.


class CaptureView(APIView):
    """Captures Video volume, Sound Volume for seamless experience"""

    parser_classes = [JSONParser]
    authentication_classes = [
        SessionAuthentication,
        JWTAuthentication,
    ]
    serializer_class = CaptureSerializer

    def get(self, request: HttpResponse):
        data, _ = CaptureModel.objects.get_or_create(user=request.user)
        serializer = CaptureSerializer(data, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: HttpResponse):
        instance = CaptureModel.objects.get_or_create(user=request.user)
        print(instance)
        serializer = CaptureSerializer(
            data=request.data,
            instance=instance,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
