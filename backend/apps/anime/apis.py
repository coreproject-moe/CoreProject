from django.urls import include, path
from rest_framework_nested import routers

from .views import (
    AnimeCharacterView,
    AnimeInfoView,
    AnimeProducerView,
    AnimeRecommendationView,
    AnimeStudioView,
    AnimeThemeView,
    EpisodeCommentView,
    EpisodeTimestampView,
    EpisodeView,
)

router = routers.SimpleRouter()
router.register(r"anime", AnimeInfoView, basename="anime_info")
anime_info_router = routers.NestedSimpleRouter(router, r"anime", lookup="anime")

#   Register Anime Info router
anime_info_router.register(r"themes", AnimeThemeView, basename="themes")
anime_info_router.register(
    r"recommendations", AnimeRecommendationView, basename="recommendations"
)
anime_info_router.register(r"episodes", EpisodeView, basename="episodes")
anime_info_router.register(r"studios", AnimeStudioView, basename="animestudiomodel")
anime_info_router.register(r"producers", AnimeProducerView, basename="producers")
anime_info_router.register(r"characters", AnimeCharacterView, basename="characters")

# Register Episode router ( subset of anime router )
episode_router = routers.NestedSimpleRouter(
    anime_info_router, r"episodes", lookup="episodes"
)
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
    path("", include(anime_info_router.urls)),
    path("", include(episode_router.urls)),
]
