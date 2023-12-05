from apps.anime.models import AnimeModel
from apps.episodes.models import EpisodeModel
from django.http import HttpRequest
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ....serializers.episode import EpisodeSerializer

# If we need to revisit, take a look at our ChadGPT conversation
# https://chat.openai.com/share/06777217-e9a9-4fb4-bcfc-28e9f59be6f8


class EpisodeAPIView(generics.ListAPIView):
    # This is due to drf-`spectacular`
    queryset = EpisodeModel.objects.none()

    serializer_class = EpisodeSerializer
    filter_backends = (DjangoFilterBackend,)
    # Permissions
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # Pagination
    pagination_class = LimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset = get_object_or_404(AnimeModel, pk=self.kwargs["pk"]).episodes.all()
        return queryset

    def post(self, request: HttpRequest, pk: int) -> Response:
        serializer: EpisodeSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        episode_instance = EpisodeModel.objects.create(**serializer.validated_data)

        AnimeModel.objects.get(pk=pk).episodes.add(episode_instance)

        return Response(status=200, data=serializer.data)
