from fastapi import APIRouter

from .avatar import router as avatar_router

router = APIRouter()
router.include_router(avatar_router)
