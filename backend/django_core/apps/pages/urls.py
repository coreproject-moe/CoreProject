from django.urls import path

from .views.anime import anime_home_view
from .views.stack import stack_view
from .views.user import login_view, logout_view

urlpatterns = [
    path("anime/", anime_home_view, name="anime_home_view"),
    path("anime/explore/", anime_home_view, name="anime_home_view"),
    path("stack/", stack_view, name="stack_view"),
    path("user/login/", login_view, name="login_view"),
    path("user/logout/", logout_view, name="logout_view"),
]
