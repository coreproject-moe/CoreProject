from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import AnilistModel, KitsuModel, MalModel
from .serializers import (
    AnilistSerializer,
    KitsuSerializer,
    MalSerializer,
    UpdateEpisodeSerializer,
)


# Create your views here.
class UpdateEpisodeView(generics.GenericAPIView):
    serializer_class = UpdateEpisodeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset()


class MalView(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = MalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        instance = MalModel.objects.filter(user=self.request.user)
        queryset = get_object_or_404(instance, user=self.request.user)
        return queryset

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=False)
        return Response(serializer.data)


class KitsuView(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = KitsuSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        instance = KitsuModel.objects.all()
        queryset = get_object_or_404(instance, user=self.request.user)
        return queryset

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=False)
        return Response(serializer.data)


class AnilistView(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = AnilistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        instance = AnilistModel.objects.all()
        queryset = get_object_or_404(instance, user=self.request.user)
        return queryset

    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)
