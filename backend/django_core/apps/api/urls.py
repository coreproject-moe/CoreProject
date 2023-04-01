from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import include, path

from .views.anime import AnimeViewSet
from .views.user import UserView

anime_router = routers.DefaultRouter()
anime_router.register(r"anime", AnimeViewSet, basename="anime")

urlpatterns = [
    path("", include(anime_router.urls)),
    path("user/", UserView.as_view()),
]

# urlpatterns = format_suffix_patterns(_urlpatterns_)
