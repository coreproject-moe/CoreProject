from apps.anime.models import AnimeModel
from apps.anime.models.anime_genre import AnimeGenreModel
from django.http import HttpRequest
from rest_framework import generics, mixins, status
from rest_framework.response import Response

from ...bases.api_view import (
    SuperUserUpdateProtectedAPIView,
    SuperUserWriteProtectedAPIView,
)
from ...serializers.anime import AnimeSerializer
from ...serializers.anime.genre import AnimeGenreSerializer


class AnimeAPIView(
    SuperUserWriteProtectedAPIView,
    generics.ListCreateAPIView,
):
    queryset = AnimeModel.objects.all()
    serializer_class = AnimeSerializer


class AnimeSpecificAPIView(
    SuperUserUpdateProtectedAPIView,
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset = AnimeModel.objects.all()
    serializer_class = AnimeSerializer


class AnimeSpecificGenreAPIView(
    SuperUserUpdateProtectedAPIView,
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    serializer_class = AnimeGenreSerializer

    def get_queryset(self):
        return (
            AnimeModel.objects.prefetch_related("genres").get(pk=self.kwargs["pk"]).genres
        )

    def get(self, *args, **kwargs) -> Response:
        return self.list(*args, **kwargs)

    def post(self, request: HttpRequest, *args, **kwargs) -> Response:
        anime_model_instance = AnimeModel.objects.prefetch_related("genres").get(
            pk=self.kwargs["pk"]
        )

        serializer: AnimeGenreSerializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance, _ = AnimeGenreModel.objects.get_or_create(**serializer.data)
            anime_model_instance.genres.add(instance)

        anime_model_instance.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
