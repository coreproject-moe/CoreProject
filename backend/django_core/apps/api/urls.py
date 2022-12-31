from ninja import NinjaAPI

from django.urls import path

api = NinjaAPI(title="CoreProjectAPI")

# Router Configurations


# ___ ANIME ROUTER _____

from .views.anime import router as anime_router
from .views.anime.anime_character import router as anime_router_anime_character_router
from .views.anime.anime_genre import router as anime_router_anime_genre_router
from .views.anime.anime_producer import router as anime_router_anime_producer_router
from .views.anime.anime_studio import router as anime_router_anime_studio_router
from .views.anime.anime_theme import router as anime_router_anime_theme_router

anime_router.add_router("", anime_router_anime_genre_router, tags=["anime_info"])
anime_router.add_router("", anime_router_anime_character_router, tags=["anime_info"])
anime_router.add_router("", anime_router_anime_producer_router, tags=["anime_info"])
anime_router.add_router("", anime_router_anime_studio_router, tags=["anime_info"])
anime_router.add_router("", anime_router_anime_theme_router, tags=["anime_info"])

from .views.anime.episode import router as anime_router_anime_episode_router
from .views.anime.episode_comment import (
    router as anime_router_anime_episode_comment_router,
)
from .views.anime.episode_timestamp import (
    router as anime_router_anime_episode_timestamp_router,
)

anime_router.add_router("", anime_router_anime_episode_router, tags=["anime_episodes"])
anime_router.add_router(
    "", anime_router_anime_episode_comment_router, tags=["anime_episodes"]
)
anime_router.add_router(
    "", anime_router_anime_episode_timestamp_router, tags=["anime_episodes"]
)

# Final route add
api.add_router("/anime", anime_router, tags=["anime_info"])

# __ CHARACTER ROUTER ___

from .views.characters import router as character_router

api.add_router("/characters", character_router, tags=["characters"])

# __ PRODUCER ROUTER ___

from .views.producers import router as producer_router

api.add_router("/producers", producer_router, tags=["producers"])


# __ STAFF ROUTER __

from .views.staffs import router as staff_router

api.add_router("/staffs", staff_router, tags=["staffs"])

# __STUDIO ROUTER ___

from .views.studios import router as studio_router

api.add_router("/studios", studio_router, tags=["studios"])

# __ TRACKER ROUTER __

from .views.trackers import router as tracker_router

api.add_router("/trackers", tracker_router, tags=["trackers"])

from .views.trackers.anilist import router as tracker_router_anilist_router
from .views.trackers.kitsu import router as tracker_router_kitsu_router
from .views.trackers.mal import router as tracker_router_myanimelist_router

tracker_router.add_router("", tracker_router_anilist_router, tags=["trackers"])
tracker_router.add_router("", tracker_router_kitsu_router, tags=["trackers"])
tracker_router.add_router("", tracker_router_myanimelist_router, tags=["trackers"])

# __ USER ROUTER __

from .views.user import router as user_router
from .views.user.login import router as user_router_login_router
from .views.user.logout import router as user_router_logout_router

user_router.add_router("", user_router_login_router, tags=["user"])
user_router.add_router("", user_router_logout_router, tags=["user"])

api.add_router("/user", user_router, tags=["user"])


urlpatterns = [
    path("", api.urls),
]
