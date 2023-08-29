from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.anime import (
    AnimeSpecificAPIView,
    AnimeViewSet,
)
from .views.anime.genre import AnimeGenresAPIView, AnimeGenresSpecificAPIView
from .views.anime.theme import AnimeThemesAPIView, AnimeThemesSpecificAPIView
from .views.user.login import LoginAPIView
from .views.user.logout import LogoutAPIView

anime_router = DefaultRouter()
anime_router.register(r"anime", AnimeViewSet, basename="anime")

urlpatterns = [
    path("", include(anime_router.urls)),
    # Anime specific routes
    path("anime/<int:pk>/", AnimeSpecificAPIView.as_view()),
    path("anime/genres/", AnimeGenresAPIView.as_view()),
    path("anime/genres/<int:pk>/", AnimeGenresSpecificAPIView.as_view()),
    path("anime/themes/", AnimeThemesAPIView.as_view()),
    path("anime/themes/<int:pk>/", AnimeThemesSpecificAPIView.as_view()),
    # User routes
    path("user/login/", LoginAPIView.as_view()),
    path("user/logout/", LogoutAPIView.as_view()),
]
