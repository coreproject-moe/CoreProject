from rest_framework import viewsets
from rest_framework import mixins
from ...serializers.user.register import RegisterSerializer
from apps.user.models import CustomUser


class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = CustomUser.objects.none()
    serializer_class = RegisterSerializer
