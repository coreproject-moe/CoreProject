from apps.comments.models import CommentModel
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from ...filters.comments import CommentFilter
from ...serializers.comments import CommentSerializer
from rest_framework import authentication, permissions
from django.http import HttpRequest
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


class CommentLikeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @method_decorator(never_cache)
    def post(request: HttpRequest, pk: int) -> Response:
        comment_instance = get_object_or_404(CommentModel, pk=pk)
        comment_instance.likes.add(request.user)
        comment_instance.save()
        return Response(status=200)

    @method_decorator(never_cache)
    def delete(request: HttpRequest, pk: int) -> Response:
        comment_instance = get_object_or_404(CommentModel, pk=pk)
        comment_instance.likes.remove(request.user)
        comment_instance.save()
        return Response(status=200)
