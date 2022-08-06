from django.shortcuts import get_object_or_404
from django.utils import timezone
from ninja import Router
from django.http import HttpRequest

from ..models import KitsuModel
from ..schemas import KitsuGETSchema, KitsuPOSTSchema

router = Router()


@router.get("/kitsu", response=KitsuGETSchema)
def get_kitsu_info(request: HttpRequest):
    response = get_object_or_404(KitsuModel, user=request.user)
    return response


@router.post("/kitsu", response=KitsuGETSchema)
def post_kitsu_info(request: HttpRequest, payload: KitsuPOSTSchema):
    instance, created = KitsuModel.objects.update_or_create(
        user=request.user,
        defaults={
            **payload.dict(),
            "created_at": timezone.now(),
        },
    )
    return instance
