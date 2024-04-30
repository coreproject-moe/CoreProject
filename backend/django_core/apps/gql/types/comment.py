import strawberry_django
from strawberry import auto
from apps.comments.models import CommentModel
from ..filters.comments import CommentFilter


@strawberry_django.type(CommentModel, filters=CommentFilter)
class Comment:
    user: auto
    text: auto

    path: str

    ratio: auto
    deleted: auto
    childrens: auto
