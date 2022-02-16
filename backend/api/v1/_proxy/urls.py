from django.urls import re_path
from .views import proxy_view

urlpatterns = [
    re_path("(?P<url>.*)/", proxy_view, name="api_proxy"),
]
