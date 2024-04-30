import strawberry_django
from apps.comments.models import CommentModel


@strawberry_django.input(CommentModel)
class CommentInput:
    text: str
    path: str | None = None

    # Optional fields since we can't do per url routes
    # model_type: Literal["anime"] | Literal["episode"] | None = None
    model_type: str | None = None
    model_pk: int | None = None
