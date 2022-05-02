from django.urls import include
from django.urls import path
from rest_framework_nested import routers

from .views import AnimeCharacterView
from .views import AnimeInfoView
from .views import AnimeProducerView
from .views import AnimeRecommendationView
from .views import AnimeStudioView
from .views import AnimeThemeView
from .views import EpisodeCommentView
from .views import EpisodeTimestampView
from .views import EpisodeView

router = routers.SimpleRouter()
router.register(r"anime", AnimeInfoView, basename="anime_info")
base_router = routers.NestedSimpleRouter(router, r"anime", lookup="anime")


base_router.register(r"themes", AnimeThemeView, basename="themes")
base_router.register(
    r"recommendations", AnimeRecommendationView, basename="recommendations"
)
base_router.register(r"episodes", EpisodeView, basename="episodes")
base_router.register(r"studios", AnimeStudioView, basename="studios")
base_router.register(r"producers", AnimeProducerView, basename="producers")
base_router.register(r"characters", AnimeCharacterView, basename="characters")

episode_router = routers.NestedSimpleRouter(base_router, r"episodes", lookup="episodes")
episode_router.register(r"comments", EpisodeCommentView, basename="episode_comments")
episode_router.register(
    r"timestamps", EpisodeTimestampView, basename="episode_timestamp"
)

# https://stackoverflow.com/questions/51823331/django-rest-framework-define-extra-arguments-using-the-action-decorator
urlpatterns = [
    path("anime/random/", AnimeInfoView.as_view({"get": "random"})),
    path(
        "anime/<str:anime_id>/episodes/<str:episode_number>/timestamps/total_watchtime/",
        EpisodeTimestampView.as_view({"get": "total_watchtime"}),
    ),
    path("", include(router.urls)),
    path("", include(base_router.urls)),
    path("", include(episode_router.urls)),
]
