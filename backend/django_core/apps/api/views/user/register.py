from rest_framework import viewsets
from rest_framework import mixins
from ...serializers.user.register import RegisterSerializer
from apps.user.models import CustomUser


class RegisterViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = CustomUser.objects.none()
    serializer_class = RegisterSerializer
