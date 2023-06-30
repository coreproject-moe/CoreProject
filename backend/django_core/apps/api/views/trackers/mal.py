from apps.trackers.models import MalModel
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.utils import timezone
from ninja import Router

from ...schemas.trackers.mal import MALGETSchema, MALPOSTSchema

router = Router()


@router.get("/mal", response=MALGETSchema)
def get_mal_info(request: HttpRequest) -> MalModel:
    response = get_object_or_404(MalModel, user=request.auth)
    return response


@router.post("/mal", response=MALGETSchema)
def post_mal_info(
    request: HttpRequest,
    payload: MALPOSTSchema,
) -> MalModel:
    instance, _ = MalModel.objects.update_or_create(
        user=request.auth,
        defaults={
            **payload.dict(),
            "created_at": timezone.now(),
        },
    )
    return instance
