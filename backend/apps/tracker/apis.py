from django.urls import path

from .views import AnilistView, KitsuView, MalView

urlpatterns = [
    path("mal/", MalView.as_view(), name="mal"),
    path("kitsu/", KitsuView.as_view(), name="kitsu"),
    path("anilist/", AnilistView.as_view(), name="anilist"),
]
