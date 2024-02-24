from django.contrib import admin

from .models import CommentModel, ReportedCommentModel


# Register your models here.
@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin[CommentModel]):
    autocomplete_fields = ["user"]
    list_filters = ["user"]
    search_fields = ["user__username", "text"]

@admin.register(ReportedCommentModel)
class ReportedCommentAdmin(admin.ModelAdmin[ReportedCommentModel]):
    autocomplete_fields = ["user"]
    search_fields = ["reason", "user__username"]