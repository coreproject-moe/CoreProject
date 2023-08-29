from apps.anime.models import AnimeModel
from rest_framework import viewsets

from ...bases.api_view import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ...serializers.anime import AnimeGETSerializer, AnimePOSTSerializer


class AnimeViewSet(viewsets.ViewSetMixin, ListCreateAPIView):
    queryset = AnimeModel.objects.all()
    serializer_class = AnimeGETSerializer


class AnimeSpecificAPIView(RetrieveUpdateDestroyAPIView):
    queryset = AnimeModel.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return AnimeGETSerializer
        else:
            return AnimePOSTSerializer


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
