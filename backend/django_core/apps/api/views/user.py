from apps.user.models import CustomUser
from rest_framework import permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.user import UserSerializer


class UserView(APIView):
    """API endpoint that allows users to be viewed or edited."""

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self) -> CustomUser:
        return CustomUser.objects.get(pk=self.request.user.pk)

    def get(self, request: Request) -> Response:
        query = self.get_object()
        serializer = UserSerializer(instance=query)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: Request) -> Response:
        # Chech this issue
        # https://github.com/encode/django-rest-framework/discussions/8862
        query = self.get_object()
        serializer = UserSerializer(instance=query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, *args, **kwargs) -> Response:
        query = self.get_object()
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
