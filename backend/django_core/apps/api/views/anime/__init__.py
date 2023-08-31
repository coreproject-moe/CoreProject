from apps.anime.models import AnimeModel
from apps.api.permissions import IsSuperUserOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from ...filters.anime import AnimeFilter
from ...serializers.anime import AnimeGETSerializer, AnimePOSTSerializer


class AnimeViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = AnimeModel.objects.all()
    serializer_class = AnimeGETSerializer
    # Filters
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AnimeFilter

    # Permissions
    permission_classes = (IsSuperUserOrReadOnly,)

    # Pagination
    pagination_class = LimitOffsetPagination


class AnimeSpecificAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnimeModel.objects.all()
    permission_classes = (IsSuperUserOrReadOnly,)

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
