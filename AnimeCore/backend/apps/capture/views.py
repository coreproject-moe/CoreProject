from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.http.response import HttpResponse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.decorators.vary import vary_on_headers

from .models import CaptureInfoModel
from .serializers import CaptureInfoSerializer

# Create your views here.


class CaptureInfoView(
    generics.GenericAPIView,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
):
    """
    AnimeCore (video player)
    ⦿   Volume
    ⦿   Timestamps

    """

    serializer_class = CaptureInfoSerializer
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
    def get(self, request: HttpResponse) -> Response:
        data, _ = CaptureInfoModel.objects.get_or_create(user=request.user)
        serializer = self.get_serializer(data, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: HttpResponse) -> Response:
        instance, _ = CaptureInfoModel.objects.get_or_create(user=request.user)
        serializer = self.get_serializer(
            data=request.data,
            instance=instance,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
