from django.urls import include, path, re_path

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

urlpatterns = [
    # Anime pages
    path(
        "anime/",
        include(
            [
                path("", anime_home_view, name="anime_home_view"),
                path(
                    "_slider/<int:pk>/",
                    anime_home_view_partial_slider_view,
                    name="anime_home_view_partial_slider_view",
                ),
                path("explore/", anime_explore_view, name="anime_explore_view"),
                path(
                    "<str:platform>/",
                    include(
                        [
                            path("<int:pk>/", anime_info_view, name="anime_info_view"),
                            path(
                                "<int:mal_id>/episode/<int:pk>/",
                                anime_episode_view,
                                name="anime_episode_view",
                            ),
                        ]
                    ),
                ),
            ]
        ),
    ),
    # Stack page
    path("stack/", stack_view, name="stack_view"),
    # User pages
    path(
        "user/",
        include(
            [
                path("login/", login_view, name="login_view"),
                path("logout/", logout_view, name="logout_view"),
                path("register/", register_view, name="register_view"),
                path("reset-password/", reset_password_view, name="reset_password_view"),
            ]
        ),
    ),
    # Upload page
    path("upload/", upload_view, name="upload_view"),
]
