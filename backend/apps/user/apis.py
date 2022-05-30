from django.urls import path

from .views import MalView, RegisterView, UserInfoView, KitsuView, AnilistView

urlpatterns = [
    path("info/", UserInfoView.as_view(), name="api_user_info"),
    path("register/", RegisterView.as_view(), name="api_register_user"),
    path("mal/", MalView.as_view(), name="mal"),
    path("kitsu/", KitsuView.as_view(), name="kitsu"),
    path("anilist/", AnilistView.as_view(), name="anilist"),
]
