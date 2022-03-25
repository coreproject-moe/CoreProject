from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AnimeInfoView

router = DefaultRouter()
router.register(r"anime", AnimeInfoView, basename="anime_info")


# https://stackoverflow.com/questions/51823331/django-rest-framework-define-extra-arguments-using-the-action-decorator
urlpatterns = [
    path(
        "anime/<int:pk>/episode/<int:episode_number>/",
        AnimeInfoView.as_view({"get": "episode"}),
    ),
    path("anime/random/", AnimeInfoView.as_view({"get": "random"})),
]

urlpatterns += router.urls
