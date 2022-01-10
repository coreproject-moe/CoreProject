from .views import *
from django.urls import path


urlpatterns = [
    path("<int:user_id>/", avatar, name="api_avatar"),
]
