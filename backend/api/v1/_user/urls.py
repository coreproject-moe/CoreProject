from django.urls import path


from .views import UserInfo

urlpatterns = [
    path("info/", UserInfo.as_view(), name="user_info"),
]
