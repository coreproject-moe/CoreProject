from fastapi import APIRouter

from .user.sign_up import router as sign_up_router

router = APIRouter()
router.include_router(sign_up_router)
