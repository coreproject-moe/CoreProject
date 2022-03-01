from django.urls import path
from .views import proxy_view

urlpatterns = [
    path("<str:secret_id>/", proxy_view, name="api_proxy"),
]
