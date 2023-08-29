from rest_framework import serializers, status, views, generics
from rest_framework.response import Response


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


class ListCreateAPIView(generics.ListCreateAPIView):
    def perform_create(self, *args, **kwargs):
        write_protected_function(*args, **kwargs)


class RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    def perform_update(self, *args, **kwargs):
        write_protected_function(*args, **kwargs)

    def perform_destroy(self: views.APIView, instance):
        if self.request.user.is_superuser:
            instance.delete()
        else:
            return Response(
                {
                    "message": "You do not have permission to create objects.",
                },
                status=status.HTTP_403_FORBIDDEN,
            )
