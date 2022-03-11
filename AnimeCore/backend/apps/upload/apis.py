from django.urls import path

from .views import AnimeInfoView

urlpatterns = [
    path("anime/<int:pk>/", AnimeInfoView.as_view(), name="api_anime_info"),
]
