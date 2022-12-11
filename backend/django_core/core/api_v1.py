from ninja import NinjaAPI
from .auth import AuthBearer

api = NinjaAPI(title="CoreProjectAPI")

# Router Configurations
# ___ DO NOT MODIFY ____


from apps.anime.api import router as anime_router
from apps.characters.api import router as character_router
from apps.producers.api import router as producer_router
from apps.staffs.api import router as staff_router
from apps.studios.api import router as studio_router
from apps.trackers.api import router as tracker_router
from apps.user.api import router as user_router

api.add_router("/anime", anime_router)
api.add_router("/characters", character_router)
api.add_router("/producers", producer_router)
api.add_router("/studios", studio_router)
api.add_router("/staffs", staff_router)

# Protected Routes
api.add_router("/trackers", tracker_router, auth=AuthBearer())
api.add_router("/user", user_router)
