from ninja import Router

router = Router()


from .user_info import router as user_router

router.add_router("", user_router)
