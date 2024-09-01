from apps.comments.models import CommentModel
from django.db.models import Count
from django.shortcuts import get_object_or_404
from strawberry import auto
import strawberry_django

from ..filters.comments import CommentFilter


@strawberry_django.type(CommentModel, filters=CommentFilter)
class CommentType:
    user: auto
    text: auto

    path: str

    deleted: auto
    childrens: auto

    ratio: auto
