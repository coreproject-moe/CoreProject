from ninja import Router
from .schemas import UserSchema
from django.contrib.auth import get_user_model

router = Router()


@router.get("/info", response=UserSchema)
def get_user_info(request):
    user = get_user_model().objects.get(username=request.user)
    return user
