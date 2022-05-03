from django.urls import path

from .views import RegisterView, UserInfoView

urlpatterns = [
    path("info/", UserInfoView.as_view(), name="api_user_info"),
    path("register/", RegisterView.as_view(), name="api_register_user"),
]
