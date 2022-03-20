from rest_framework.routers import DefaultRouter

from .views import CaptureTimeStampView, CaptureVolumeView

router = DefaultRouter()
router.register(r"anime", CaptureTimeStampView, basename="capture_timestamp")
router.register(r"volume", CaptureVolumeView, basename="capture_volume")
urlpatterns = router.urls
