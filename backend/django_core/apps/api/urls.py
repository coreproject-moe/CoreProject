from django.urls import path
from django.utils.module_loading import import_string
from ninja import NinjaAPI

from .parser import CustomParser

api = NinjaAPI(
    title="CoreProjectAPI",
    parser=CustomParser(),
)

# Router Configurations


# ___ ANIME ROUTER _____

from .views.anime import router as anime_router

api.add_router(
    "/anime",
    anime_router,
    tags=["anime_info"],
)
anime_router.add_router(
    "",
    import_string(
        "apps.api.views.anime.genres.router",
    ),
    tags=["anime_info"],
)
anime_router.add_router(
    "",
    import_string(
        "apps.api.views.anime.themes.router",
    ),
    tags=["anime_info"],
)
anime_router.add_router(
    "",
    import_string(
        "apps.api.views.anime.anime_staff.router",
    ),
    tags=["anime_info"],
)
anime_router.add_router(
    "",
    import_string(
        "apps.api.views.anime.anime_genre.router",
    ),
    tags=["anime_info"],
)
anime_router.add_router(
    "",
    import_string(
        "apps.api.views.anime.anime_character.router",
    ),
    tags=["anime_info"],
)
anime_router.add_router(
    "",
    import_string(
        "apps.api.views.anime.anime_producer.router",
    ),
    tags=["anime_info"],
)
anime_router.add_router(
    "",
    import_string(
        "apps.api.views.anime.anime_studio.router",
    ),
    tags=["anime_info"],
)
anime_router.add_router(
    "",
    import_string(
        "apps.api.views.anime.anime_theme.router",
    ),
    tags=["anime_info"],
)
anime_router.add_router(
    "",
    import_string("apps.api.views.anime.openings.router"),
    tags=["anime_info"],
)
anime_router.add_router(
    "",
    import_string("apps.api.views.anime.anime_openings.router"),
    tags=["anime_info"],
)
anime_router.add_router(
    "",
    import_string("apps.api.views.anime.endings.router"),
    tags=["anime_info"],
)
anime_router.add_router(
    "",
    import_string("apps.api.views.anime.anime_endings.router"),
    tags=["anime_info"],
)
# Episodes

anime_router.add_router(
    "",
    import_string(
        "apps.api.views.anime.episode.router",
    ),
    tags=["episodes"],
)
anime_router.add_router(
    "",
    import_string(
        "apps.api.views.anime.episode_comment.router",
    ),
    tags=["episodes"],
)
anime_router.add_router(
    "",
    import_string(
        "apps.api.views.anime.episode_timestamp.router",
    ),
    tags=["episodes"],
)


# __ CHARACTER ROUTER ___

from .views.characters import router as character_router

api.add_router(
    "/characters",
    character_router,
    tags=["characters"],
)

# __ PRODUCER ROUTER ___

from .views.producers import router as producer_router

api.add_router(
    "/producers",
    producer_router,
    tags=["producers"],
)


# __ STAFF ROUTER __

from .views.staffs import router as staff_router

api.add_router(
    "/staffs",
    staff_router,
    tags=["staffs"],
)

# __ USER ROUTER __

from .views.user import router as user_router

api.add_router("/user", user_router, tags=["user"])

user_router.add_router(
    "",
    import_string(
        "apps.api.views.user.login.router",
    ),
    tags=["user"],
)
user_router.add_router(
    "",
    import_string(
        "apps.api.views.user.logout.router",
    ),
    tags=["user"],
)
user_router.add_router(
    "",
    import_string(
        "apps.api.views.user.signup.router",
    ),
    tags=["user"],
)
user_router.add_router(
    "/username_validity",
    import_string(
        "apps.api.views.user.username_validity.router",
    ),
    tags=["user"],
)
# __ TRACKER ROUTER __

from .views.trackers import router as tracker_router

api.add_router(
    "/trackers",
    tracker_router,
    tags=["trackers"],
)

tracker_router.add_router(
    "",
    import_string(
        "apps.api.views.trackers.anilist.router",
    ),
    tags=["trackers"],
)
tracker_router.add_router(
    "",
    import_string(
        "apps.api.views.trackers.kitsu.router",
    ),
    tags=["trackers"],
)
tracker_router.add_router(
    "",
    import_string(
        "apps.api.views.trackers.mal.router",
    ),
    tags=["trackers"],
)


# __ EPISODE ROUTER ___
from .views.episodes.comment import router as episode_comment_router

api.add_router(
    "/episode/comment",
    episode_comment_router,
    tags=["episodes"],
)


# __ FEED ROUTER __
# May be powered by Machine learning in future
from .views.feeds.featured import router as feature_router

api.add_router(
    "/feed/featured",
    feature_router,
    tags=["feed"],
)
from .views.feeds.all import router as all_router

api.add_router("/feed/all", all_router, tags=["feed"])


# __ STATS ROUTER __
from .views.stats import router as stats_router

api.add_router(
    "/stats/anime",
    stats_router,
    tags=["stats"],
)

urlpatterns = [
    path(
        "v1/",
        api.urls,
    ),
]
