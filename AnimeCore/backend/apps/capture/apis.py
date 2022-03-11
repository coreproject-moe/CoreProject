from django.urls import path
from .views import CaptureVideoView

urlpatterns = [
    path(
        "",
        CaptureVideoView.as_view(),
        name="api_capture_video",
    ),
]
