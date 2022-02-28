from django.urls import path
from .views import *


urlpatterns = [
    path("user_info/", user_edit_info_page, name="user_edit_info_page"),
]
