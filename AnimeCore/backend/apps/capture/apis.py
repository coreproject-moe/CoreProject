from django.urls import path
from .views import CaptureInfoView

urlpatterns = [
    path(
        "",
        CaptureInfoView.as_view(),
        name="api_capture_video",
    ),
]
