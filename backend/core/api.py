from apps.api.v1.anime.api import router as anime_router
from apps.api.v1.trackers.api import router as tracker_router
from apps.api.v1.user.api import router as user_router
from apps.api.v1.characters.api import router as character_router
from ninja import NinjaAPI
from ninja.security import django_auth

api = NinjaAPI(csrf=True, title="CoreProjectAPI")

api.add_router("/anime", anime_router)
api.add_router("/user", user_router, auth=django_auth)
api.add_router("/trackers", tracker_router, auth=django_auth)
api.add_router("/characters", character_router)
