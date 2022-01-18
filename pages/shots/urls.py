from django.urls import path
from .views import *

urlpatterns = [
    path("", shots_home_page, name="shots_home_page"),
]
