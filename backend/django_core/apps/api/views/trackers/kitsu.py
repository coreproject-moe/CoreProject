from apps.trackers.models import KitsuModel
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.utils import timezone
from ninja import Router

from ...schemas.trackers.kitsu import KitsuGETSchema, KitsuPOSTSchema

router = Router()


@router.get("/kitsu", response=KitsuGETSchema)
def get_kitsu_info(request: HttpRequest) -> KitsuModel:
    response = get_object_or_404(KitsuModel, user=request.auth)
    return response


@router.post("/kitsu", response=KitsuGETSchema)
def post_kitsu_info(request: HttpRequest, payload: KitsuPOSTSchema) -> KitsuModel:
    instance, _ = KitsuModel.objects.update_or_create(
        user=request.auth,
        defaults={
            **payload.dict(),
            "created_at": timezone.now(),
        },
    )
    return instance
