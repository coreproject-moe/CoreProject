from rest_framework import serializers


class CommentReactionSerializer(serializers.Serializer):
    reaction = serializers.CharField()
