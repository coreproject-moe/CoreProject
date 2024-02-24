from rest_framework.serializers import ModelSerializer

from apps.comments.models import ReportedCommentModel

class CommentReportSerializer(ModelSerializer):
    class Meta:
        model = ReportedCommentModel
        fields = "__all__"