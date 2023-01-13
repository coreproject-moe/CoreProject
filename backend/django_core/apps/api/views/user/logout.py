from apps.user.models import Token
from core.auth import AuthBearer
from django.http import HttpRequest, HttpResponse
from ninja import Router

router = Router()


@router.delete("/logout", auth=AuthBearer())
def post_user_logout_info(request: HttpRequest):
    token: Token = Token.objects.get(user=request.auth)
    token.delete()
    return HttpResponse("Successful", status=200)
