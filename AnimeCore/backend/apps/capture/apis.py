from django.urls import path
from .views import CaptureVolumeView

urlpatterns = [
    path("video_volume/", CaptureVolumeView.as_view(), name="api_capture_video_volume"),
]
