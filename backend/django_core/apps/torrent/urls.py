from django.urls import path
from .views import AnnounceView, TorrentView

urlpatterns = [
    path("announce/", AnnounceView.as_view(), name="announce"),
    path("list/", TorrentView.as_view(), name="list"),
]
