from django.urls import path
from .views import *


urlpatterns = [
    path("user_info/", user_info_edit_page, name="user_info_edit_page"),
]
