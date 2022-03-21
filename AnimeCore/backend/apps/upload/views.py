from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import action

from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend

from .models import AnimeInfoModel
from .serializers import AnimeInfoSerializer

# Create your views here.


class AnimeInfoView(generics.ListAPIView):

    serializer_class = AnimeInfoSerializer
    filterset_fields = ["episodes", "mal_id", "id"]

    def get_queryset(self, *args, **kwargs):
        queryset = AnimeInfoModel.objects.all()

        mal_id = self.request.query_params.get("mal_id")
        if mal_id:
            queryset = queryset.filter(mal_id__in=mal_id.split(","))

        __id = self.request.query_params.get("id")
        if __id:
            queryset = queryset.filter(id__in=__id.split(","))

        newest_first = self.request.query_params.get("newest_first")
        if newest_first:
            queryset = queryset.order_by("-updated")

        return queryset

    def get(self, request: HttpRequest) -> Response:
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
