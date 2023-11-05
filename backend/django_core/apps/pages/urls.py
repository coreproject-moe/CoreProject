from django.urls import path

from .views.anime import anime_home_view, anime_info_view
from .views.stack import stack_view
from .views.user import login_view, logout_view, register_view, reset_password_view

urlpatterns = [
    # Anime pages
    path("anime/", anime_home_view, name="anime_home_view"),
    path("anime/explore/", anime_home_view, name="anime_explore_view"),
    path("anime/mal/<int:pk>/", anime_info_view, name="anime_info_view"),
    # Stack page
    path("stack/", stack_view, name="stack_view"),
    # User pages
    path("user/login/", login_view, name="login_view"),
    path("user/logout/", logout_view, name="logout_view"),
    path("user/register/", register_view, name="register_view"),
    path("user/reset-password/", reset_password_view, name="reset_password_view"),
]
