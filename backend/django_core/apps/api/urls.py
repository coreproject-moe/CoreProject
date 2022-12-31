from ninja import NinjaAPI
from django.urls import path

api = NinjaAPI(title="CoreProjectAPI")

# Router Configurations
# ___ DO NOT MODIFY ____


from .views.anime import router as anime_router
from .views.characters import router as character_router
from .views.producers import router as producer_router
from .views.staffs import router as staff_router
from .views.studios import router as studio_router
from .views.trackers import router as tracker_router
from .views.user import router as user_router

api.add_router("/anime", anime_router)
api.add_router("/characters", character_router)
api.add_router("/producers", producer_router)
api.add_router("/studios", studio_router)
api.add_router("/staffs", staff_router)

# Protected Routes
api.add_router("/trackers", tracker_router)
api.add_router("/user", user_router)

urlpatterns = [
    path("", api.urls),
]
