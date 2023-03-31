from rest_framework import routers

from django.urls import include, path

from .views.user import UserView
from rest_framework.urlpatterns import format_suffix_patterns

_urlpatterns_ = [
    path("user/", UserView.as_view()),
]

urlpatterns = format_suffix_patterns(_urlpatterns_)
