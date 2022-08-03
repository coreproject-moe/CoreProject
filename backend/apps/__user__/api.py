from ninja import Router
from ninja.security import HttpBearer

router = Router()


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token


@router.get("/bearer", auth=AuthBearer())
def bearer(request):
    return {"token": request.auth}
