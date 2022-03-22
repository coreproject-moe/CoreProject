from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AnimeInfoView

router = DefaultRouter()
router.register(r"anime", AnimeInfoView, basename="anime_info")


# https://stackoverflow.com/questions/51823331/django-rest-framework-define-extra-arguments-using-the-action-decorator
urlpatterns = [
    path(
        "anime/<int:pk>/episode/",
        AnimeInfoView.as_view({"get": "episode"}),
        name="episode_info",
    ),
    path(
        "anime/<int:pk>/episode/<int:episode_number>/",
        AnimeInfoView.as_view({"get": "episode_list"}),
        name="episode_info",
    ),
]

urlpatterns += router.urls
