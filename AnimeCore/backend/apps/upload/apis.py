from django.urls import path

from .views import AnimeInfo

urlpatterns = [
    path("anime/<int:pk>/", AnimeInfo.as_view(), name="api_anime_info"),
]
