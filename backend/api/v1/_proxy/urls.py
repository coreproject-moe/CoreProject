from django.urls import path
from .views import proxy_view

urlpatterns = [path("", proxy_view, name="api_proxy")]
