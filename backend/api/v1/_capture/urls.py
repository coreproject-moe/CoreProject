from django.urls import path
from .views import CaptureView

urlpatterns = [
    path("", CaptureView.as_view(), name="capture"),
]
