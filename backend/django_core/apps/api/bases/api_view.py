from rest_framework import serializers
from rest_framework.response import Response
from typing import NoReturn
from rest_framework import views
from rest_framework import status


def write_protected_function(self: views.APIView, serializer: serializers.ModelSerializer):
    # Check if the user is a superuser
    if self.request.user.is_superuser:
        serializer.save()
    else:
        return Response(
            {
                "message": "You do not have permission to create objects.",
            },
            status=status.HTTP_403_FORBIDDEN,
        )


class SuperUserWriteProtectedAPIView:
    ...


SuperUserWriteProtectedAPIView.perform_update = write_protected_function
SuperUserWriteProtectedAPIView.perform_create = write_protected_function
