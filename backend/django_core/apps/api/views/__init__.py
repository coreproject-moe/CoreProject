from apps.anime.models import AnimeModel
from rest_framework import generics

from ..bases.api_view import SuperUserWriteProtectedAPIView
from ..serializers.anime import AnimeSerializer


class AnimeAPIView(generics.ListCreateAPIView, SuperUserWriteProtectedAPIView):
    queryset = AnimeModel.objects.all()
    serializer_class = AnimeSerializer


class AnimeSpecificAPIView(
    generics.RetrieveUpdateDestroyAPIView, SuperUserWriteProtectedAPIView
):
    queryset = AnimeModel.objects.all()
    serializer_class = AnimeSerializer
