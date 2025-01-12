from django.urls import path
from .views import announce_view, TorrentView

urlpatterns = [
    path("announce/", announce_view, name="announce"),
    path("list/", TorrentView.as_view(), name="list"),
]
