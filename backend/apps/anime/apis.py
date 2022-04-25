from django.urls import path, include
from rest_framework_nested import routers


from .views import (
    AnimeInfoView,
    AnimeThemeView,
    AnimeStudioView,
    AnimeProducerView,
    AnimeRecommendationView,
    EpisodeView,
    EpisodeCommentView,
    EpisodeTimestampView,
)

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


episode_router = routers.NestedSimpleRouter(base_router, r"episodes", lookup="episodes")
episode_router.register(r"comments", EpisodeCommentView, basename="episode_comments")
episode_router.register(
    r"timestamps", EpisodeTimestampView, basename="episode_timestamp"
)

# https://stackoverflow.com/questions/51823331/django-rest-framework-define-extra-arguments-using-the-action-decorator
urlpatterns = [
    path("anime/random/", AnimeInfoView.as_view({"get": "random"})),
    path("", include(router.urls)),
    path("", include(base_router.urls)),
    path("", include(episode_router.urls)),
]
