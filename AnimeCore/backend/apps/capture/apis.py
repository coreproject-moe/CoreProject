from django.urls import path
from .views import CaptureVideoVolumeView, CaptureVideoTimeStampView

urlpatterns = [
    path(
        "video_volume/",
        CaptureVideoVolumeView.as_view(),
        name="api_capture_video_volume",
    ),
    path(
        "video_timestamp/",
        CaptureVideoTimeStampView.as_view(),
        name="api_capture_video_timestamp",
    ),
]
