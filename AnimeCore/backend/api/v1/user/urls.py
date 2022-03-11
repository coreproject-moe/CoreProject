from django.urls import path
from .views import UserInfo

urlpatterns = [
    path("info/", UserInfo.as_view(), name="api_user_info"),
]
