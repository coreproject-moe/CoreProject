from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.decorators.vary import vary_on_headers

from .models import CaptureTimeStampModel
from .serializers import CaptureTimeStampSerializer

# Create your views here.


class CaptureTimeStampView(viewsets.ViewSet):
    """
    AnimeCore (video player)
    ⦿   Timestamps

    """

    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        JWTAuthentication,
        SessionAuthentication,
    ]

    @method_decorator(cache_page(5))
    @method_decorator(
        vary_on_headers(
            "Authorization",
        )
    )
    def list(self, request: HttpRequest) -> Response:
        queryset = CaptureTimeStampModel.objects.all()
        serializer = CaptureTimeStampSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request: HttpRequest, pk: int) -> Response:
        queryset = CaptureTimeStampModel.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CaptureTimeStampSerializer(user)
        return Response(serializer.data)
