from django.shortcuts import get_object_or_404
from django.utils import timezone
from ninja import Router
from django.http import HttpRequest

from ..models import MalModel
from ..schemas import MALGETSchema, MALPOSTSchema

router = Router()


@router.get("/mal", response=MALGETSchema)
def get_mal_info(request: HttpRequest):
    response = get_object_or_404(MalModel, user=request.user)
    return response


@router.post("/mal", response=MALGETSchema)
def post_mal_info(request: HttpRequest, payload: MALPOSTSchema):
    instance, created = MalModel.objects.update_or_create(
        user=request.user,
        defaults={
            **payload.dict(),
            "created_at": timezone.now(),
        },
    )
    return instance
