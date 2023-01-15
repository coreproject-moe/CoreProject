from apps.trackers.models import AnilistModel
from ninja import Router

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.utils import timezone

from ...schemas.trackers import AnilistGETSchema, AnilistPOSTSchema

router = Router()


@router.get("/anilist", response=AnilistGETSchema)
def get_anilist_info(request: HttpRequest):
    response = get_object_or_404(AnilistModel, user=request.auth)
    return response


@router.post("/anilist", response=AnilistGETSchema)
@login_required
def post_anilist_info(request: HttpRequest, payload: AnilistPOSTSchema):
    instance, _ = AnilistModel.objects.update_or_create(
        user=request.auth,
        defaults={
            **payload.dict(),
            "created_at": timezone.now(),
        },
    )
    return instance
