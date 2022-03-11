from django.urls import path
from .views import UserInfo, Register

urlpatterns = [
    path("info/", UserInfo.as_view(), name="api_user_info"),
    path("register/", Register.as_view(), name="api_register_user"),
]
