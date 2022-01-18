from django.urls import path
from .views import *

urlpatterns = [
    path("", ost_home_page, name="ost_home_page"),
]
