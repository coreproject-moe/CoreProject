from django.shortcuts import get_object_or_404
import strawberry_django
from strawberry import auto
from apps.comments.models import CommentModel
from ..filters.comments import CommentFilter
from django.db.models import Count


@strawberry_django.type(CommentModel, filters=CommentFilter)
class CommentType:
    user: auto
    text: auto

    path: str

    deleted: auto
    childrens: auto

    ratio: auto
