from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.anime import (
    AnimeSpecificAPIView,
    AnimeViewSet,
)
from .views.anime.episode import EpisodeAPIView
from .views.anime.episode.comment import EpisodeCommentAPIView
from .views.anime.episode.timestamp import EpisodeTimeStampAPIView
from .views.anime.genre import AnimeGenresAPIView, AnimeGenresSpecificAPIView
from .views.anime.theme import AnimeThemesAPIView, AnimeThemesSpecificAPIView
from .views.characters import CharacterViewSet
from .views.producers import ProducerViewSet
from .views.staffs import StaffViewSet
from .views.user.login import LoginAPIView
from .views.user.logout import LogoutAPIView

base_router = DefaultRouter()
base_router.register(r"anime", AnimeViewSet, basename="anime")
base_router.register(r"character", CharacterViewSet, basename="character")
base_router.register(r"producer", ProducerViewSet, basename="producer")
base_router.register(r"staff", StaffViewSet, basename="staff")

urlpatterns = [
    path("", include(base_router.urls)),
    # Anime specific routes
    path("anime/genres/", AnimeGenresAPIView.as_view()),
    path("anime/genres/<int:pk>/", AnimeGenresSpecificAPIView.as_view()),
    path("anime/themes/", AnimeThemesAPIView.as_view()),
    path("anime/themes/<int:pk>/", AnimeThemesSpecificAPIView.as_view()),
    # Episode
    path(
        "anime/<int:pk>/episode/",
        EpisodeAPIView.as_view(),
    ),
    path(
        "anime/<int:pk>/episode/<int:episode_number>/comment",
        EpisodeCommentAPIView.as_view(),
    ),
    path(
        "anime/<int:pk>/episode/<int:episode_number>/timestamp",
        EpisodeTimeStampAPIView.as_view(),
    ),
    # User routes
    path("user/login/", LoginAPIView.as_view()),
    path("user/logout/", LogoutAPIView.as_view()),
]
