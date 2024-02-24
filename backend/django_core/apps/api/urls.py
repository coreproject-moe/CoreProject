from django.urls import include, path
from rest_framework import routers


from .views.user.register import RegisterViewSet
from .views.user.validity.username import UsernameValiditiyAPIView
from .views.user.validity.email import EmailValiditiyAPIView
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
from .views.comment.report import CommentReportAPIView
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

user_router = routers.DefaultRouter()
user_router.register(r"user/register", RegisterViewSet, basename="register")

# https://stackoverflow.com/a/65186703
base_router.registry.extend(user_router.registry)

urlpatterns = [
    # Routers
    path("", include(base_router.urls)),
    # Anime specific routes
    path("anime/", include([
        path(
            "<int:pk>/comment",
            AnimeCommentAPIView.as_view(),
            name="anime-commment-endpoint",
        ),
        path("genres/", AnimeGenresAPIView.as_view()),
        path("genres/<int:pk>/", AnimeGenresSpecificAPIView.as_view()),
        path("themes/", AnimeThemesAPIView.as_view()),
        path("themes/<int:pk>/", AnimeThemesSpecificAPIView.as_view()),
    ])),
    # Episode
    path("anime/<int:pk>/episode/", include([
        path("", EpisodeAPIView.as_view()),
        path(
            "<int:episode_number>/comment",
            EpisodeCommentAPIView.as_view(),
            name="episode-comment-endpoint",
        ),
        path(
            "<int:episode_number>/timestamp",
            EpisodeTimeStampAPIView.as_view(),
        ),
    ])),
    # User routes
    path("user/", include([
        path("login/", LoginAPIView.as_view(), name="login-endpoint"),
        path("logout/", LogoutAPIView.as_view(), name="logout-endpoint"),
        path(
            "validity/username",
            UsernameValiditiyAPIView.as_view(),
            name="username-validity-endpoint",
        ),
        path(
            "validity/email",
            EmailValiditiyAPIView.as_view(),
            name="email-validity-endpoint",
        ),
    ])),
    # Comment routes
    path("comment/<int:pk>/", include([
        path(
            "reaction/",
            CommentReactionAPIView.as_view(),
            name="comment-reaction-endpoint",
        ),
        path(
            "report/",
            CommentReportAPIView.as_view(),
            name="comment-report-endpoint",
        ),
    ])),
    # Upload route
    path(
        "upload/",
        DoodstreamAPIView.as_view(),
        name="doodstream-provider-endpoint",
    ),
]
