from django.contrib import admin

from .models import CommentModel


# Register your models here.
@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin[CommentModel]):
    autocomplete_fields = ["user"]
    list_filters = ["user"]
    search_fields = ["user__username", "text"]
