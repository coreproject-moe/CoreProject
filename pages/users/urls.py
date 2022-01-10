from django.urls import path
from .views import *


urlpatterns = [
    path("edit_info/", user_edit_info_page, name="user_edit_info_page"),
]
