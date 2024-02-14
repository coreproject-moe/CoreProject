from django.urls import include, path
from rest_framework import routers

from .views.user.username_validity import UsernameValiditiyAPIView
from .views.anime import AnimeViewSet
from .views.anime.comment import AnimeCommentAPIView
from .views.anime.episode import EpisodeAPIView
from .views.anime.episode.comment import EpisodeCommentAPIView
from .views.anime.episode.timestamp import EpisodeTimeStampAPIView
from .views.anime.genre import AnimeGenresAPIView, AnimeGenresSpecificAPIView
from .views.anime.theme import AnimeThemesAPIView, AnimeThemesSpecificAPIView
from .views.characters import CharacterViewSet
from .views.comment import CommentViewSet
from .views.comment.reaction import CommentReactionAPIView
from .views.producers import ProducerViewSet
from .views.staffs import StaffViewSet
from .views.user.login import LoginAPIView
from .views.user.logout import LogoutAPIView
from .views.upload.doodstream import DoodstreamAPIView

base_router = routers.DefaultRouter()
base_router.register(r"comments", CommentViewSet, basename="comment")
base_router.register(r"anime", AnimeViewSet, basename="anime")
base_router.register(r"character", CharacterViewSet, basename="character")
base_router.register(r"producer", ProducerViewSet, basename="producer")
base_router.register(r"staff", StaffViewSet, basename="staff")

urlpatterns = [
    path("", include(base_router.urls)),
    # Anime specific routes
    path(
        "anime/<int:pk>/comment",
        AnimeCommentAPIView.as_view(),
        name="anime-commment-endpoint",
    ),
    path("anime/genres/", AnimeGenresAPIView.as_view()),
    path("anime/genres/<int:pk>/", AnimeGenresSpecificAPIView.as_view()),
    path("anime/themes/", AnimeThemesAPIView.as_view()),
    path("anime/themes/<int:pk>/", AnimeThemesSpecificAPIView.as_view()),
    # Episode
    path(
        "anime/<int:pk>/episode/",
        EpisodeAPIView.as_view(),
    ),
    path(
        "anime/<int:pk>/episode/<int:episode_number>/comment",
        EpisodeCommentAPIView.as_view(),
        name="episode-comment-endpoint",
    ),
    path(
        "anime/<int:pk>/episode/<int:episode_number>/timestamp",
        EpisodeTimeStampAPIView.as_view(),
    ),
    # User routes
    path("user/login/", LoginAPIView.as_view(), name="login-endpoint"),
    path("user/logout/", LogoutAPIView.as_view(), name="logout-endpoint"),
    path(
        "user/username_validity",
        UsernameValiditiyAPIView.as_view(),
        name="username-validity-endpoint",
    ),
    # Comment routes
    path(
        "comment/<int:pk>/reaction/",
        CommentReactionAPIView.as_view(),
        name="comment-reaction-endpoint",
    ),
    # Upload route
    path(
        "upload/",
        DoodstreamAPIView.as_view(),
        name="doodstream-provider-endpoint",
    ),
]
