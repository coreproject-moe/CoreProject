from ninja import NinjaAPI, Router

router = Router()


@router.get("/hello")
def hello(request):
    return "Hello world"
