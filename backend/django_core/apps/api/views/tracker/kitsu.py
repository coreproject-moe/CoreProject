from ninja import Router

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.utils import timezone

from apps.trackers.models import KitsuModel
from ...schemas.tracker import KitsuGETSchema, KitsuPOSTSchema

router = Router()


@router.get("/kitsu", response=KitsuGETSchema)
def get_kitsu_info(request: HttpRequest):
    response = get_object_or_404(KitsuModel, user=request.auth)
    return response


@router.post("/kitsu", response=KitsuGETSchema)
@login_required
def post_kitsu_info(request: HttpRequest, payload: KitsuPOSTSchema):
    instance, created = KitsuModel.objects.update_or_create(
        user=request.auth,
        defaults={
            **payload.dict(),
            "created_at": timezone.now(),
        },
    )
    return instance
