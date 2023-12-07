from apps.comments.models import CommentModel
from apps.user.models import CustomUser
from django.http import HttpRequest
from rest_framework import serializers


class CommentReactionSerializer(serializers.Serializer):
    reaction = serializers.CharField()
