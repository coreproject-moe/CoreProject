from apps.__user__.api import router as user_router
from apps.api.v1.anime.api import router as anime_router
from ninja import NinjaAPI

api = NinjaAPI()
api.add_router("/anime", anime_router)
api.add_router("/user", user_router)
