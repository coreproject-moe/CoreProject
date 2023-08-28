from apps.anime.models import AnimeModel
from apps.anime.models.anime_genre import AnimeGenreModel
from apps.anime.models.anime_theme import AnimeThemeModel
from django.http import HttpRequest
from rest_framework import generics, mixins, status
from rest_framework.response import Response

from ...bases.api_view import (
    SuperUserUpdateProtectedAPIView,
    SuperUserWriteProtectedAPIView,
)
from ...serializers.anime import AnimeSerializer
from ...serializers.anime.genre import AnimeGenreSerializer
from ...serializers.anime.theme import AnimeThemeSerializer


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


# class AnimeSpecificThemeAPIView(
#     SuperUserUpdateProtectedAPIView,
#     mixins.ListModelMixin,
#     generics.GenericAPIView,
# ):
#     serializer_class = AnimeThemeSerializer

#     def get_queryset(self) -> AnimeModel:
#         return (
#             AnimeModel.objects.prefetch_related("themes").get(pk=self.kwargs["pk"]).themes
#         )

#     def get(self, *args, **kwargs) -> Response:
#         return self.list(*args, **kwargs)

#     def post(self, request: HttpRequest, *args, **kwargs) -> Response:
#         anime_model_instance = AnimeModel.objects.get(pk=self.kwargs["pk"])

#         serializer: AnimeGenreSerializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             instance, _ = AnimeThemeModel.objects.get_or_create(**serializer.data)
#             anime_model_instance.themes.add(instance)

#         anime_model_instance.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
