from django.urls import path

from .views.anime import (
    anime_episode_view,
    anime_explore_view,
    anime_home_view,
    anime_home_view_partial_slider_view,
    anime_info_view,
)
from .views.stack import stack_view
from .views.upload import upload_view
from .views.user import login_view, logout_view, register_view, reset_password_view
from .views.partial import markdown_endpoint

urlpatterns = [
    # Anime pages
    path("anime/", anime_home_view, name="anime_home_view"),
    path(
        "anime/_slider/<int:pk>/",
        anime_home_view_partial_slider_view,
        name="anime_home_view_partial_slider_view",
    ),
    path("anime/explore/", anime_explore_view, name="anime_explore_view"),
    # Anime info page
    path("anime/mal/<int:pk>/", anime_info_view, name="anime_info_view"),
    # Anime episode page
    path(
        "anime/mal/<int:mal_id>/episode/<int:pk>/",
        anime_episode_view,
        name="anime_episode_view",
    ),
    # Stack page
    path("stack/", stack_view, name="stack_view"),
    # User pages
    path("user/login/", login_view, name="login_view"),
    path("user/logout/", logout_view, name="logout_view"),
    path("user/register/", register_view, name="register_view"),
    path("user/reset-password/", reset_password_view, name="reset_password_view"),
    # Upload page
    path("upload/", upload_view, name="upload_view"),
    # Partials
    path("partials/markdown", markdown_endpoint, name="partial_markdown_endpoint"),
]
