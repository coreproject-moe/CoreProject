from django.urls import path, include
from rest_framework_nested import routers

from .views import AnimeInfoView, EpisodeView, EpisodeCommentView

router = routers.SimpleRouter()
router.register(r"anime", AnimeInfoView, basename="anime_info")

episode_router = routers.NestedSimpleRouter(router, r"anime", lookup="anime")
episode_router.register(r"episodes", EpisodeView, basename="episodes")

episode_comment_router = routers.NestedSimpleRouter(
    episode_router, r"episodes", lookup="episodes"
)
episode_comment_router.register(
    r"comments", EpisodeCommentView, basename="episode_comments"
)

# https://stackoverflow.com/questions/51823331/django-rest-framework-define-extra-arguments-using-the-action-decorator
urlpatterns = [
    path("anime/random/", AnimeInfoView.as_view({"get": "random"})),
    path("", include(router.urls)),
    path("", include(episode_router.urls)),
    path("", include(episode_comment_router.urls)),
]
