from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from apps.comments.models import CommentModel, ReportedCommentModel
from ...serializers.comments.report import CommentReportSerializer

class CommentReportAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request: HttpRequest, pk: int):
        comment_instance = get_object_or_404(CommentModel, pk=pk)
        report_comment_instance, created = ReportedCommentModel.objects.get_or_create(comment=comment_instance)
        
        if not report_comment_instance.reports.filter(pk=request.user.pk).exists():
            report_comment_instance.reports.add(request.user)
            report_comment_instance.save()

        serializer = CommentReportSerializer(report_comment_instance)
        return Response(status=200, data=serializer.data)