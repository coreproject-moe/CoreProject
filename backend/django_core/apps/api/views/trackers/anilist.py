from apps.trackers.models import AnilistModel
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.utils import timezone
from ninja import Router

from ...schemas.trackers.anilist import AnilistGETSchema, AnilistPOSTSchema

router = Router()


@router.get("/anilist", response=AnilistGETSchema)
def get_anilist_info(request: HttpRequest) -> AnilistModel:
    response = get_object_or_404(AnilistModel, user=request.auth)
    return response


@router.post("/anilist", response=AnilistGETSchema)
def post_anilist_info(request: HttpRequest, payload: AnilistPOSTSchema) -> AnilistModel:
    instance, _ = AnilistModel.objects.update_or_create(
        user=request.auth,
        defaults={
            **payload.dict(),
            "created_at": timezone.now(),
        },
    )
    return instance
