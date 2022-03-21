from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AnimeInfoView

urlpatterns = [
    path("anime/", AnimeInfoView.as_view(), name="anime_info"),
]
