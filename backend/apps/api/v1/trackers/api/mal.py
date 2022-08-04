from ..models import MalModel
from django.shortcuts import get_object_or_404
from ninja import Router
from django.utils import timezone

from ..schemas import MALGETSchema, MALPOSTSchema

router = Router()


@router.get("/mal", response=MALGETSchema)
def get_mal_info(request):
    response = get_object_or_404(MalModel, user=request.user)
    return response


@router.post("/mal", response=MALGETSchema)
def post_mal_info(request, payload: MALPOSTSchema):
    response, _ = MalModel.objects.update_or_create(
        user=request.user,
        defaults={
            **payload.dict(),
            "created_at": timezone.now(),
        },
    )
    return response
