from rest_framework import status
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

from .models import CaptureTimeStampModel, CaptureVolumeModel
from .serializers import CaptureTimeStampSerializer, CaptureVolumeSerializer

# Create your views here.


class CaptureVolumeView(viewsets.ViewSet):
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

    @method_decorator(cache_page(5))
    @method_decorator(
        vary_on_headers(
            "Authorization",
        )
    )
    def list(self, request: HttpRequest) -> Response:
        queryset = CaptureVolumeModel.objects.all()
        volume = get_object_or_404(queryset, user=request.user)
        serializer = CaptureVolumeSerializer(volume)
        return Response(serializer.data)

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


class CaptureTimeStampView(viewsets.GenericViewSet):
    """
    AnimeCore (video player)
    ⦿   Timestamps

    """

    queryset = CaptureTimeStampModel.objects.all()
    serializer_class = CaptureTimeStampSerializer
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
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @method_decorator(cache_page(5))
    @method_decorator(
        vary_on_headers(
            "Authorization",
        )
    )
    def retrieve(self, request: HttpRequest, pk: int) -> Response:
        queryset = self.get_queryset()
        timestamps = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(timestamps)
        return Response(serializer.data)

    def partial_update(self, request: HttpRequest, pk=None):
        queryset = self.get_queryset()
        timestamps = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(
            instance=timestamps,
            data=request.data,
            partial=True,
            context={
                "user": request.user,
            },
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
