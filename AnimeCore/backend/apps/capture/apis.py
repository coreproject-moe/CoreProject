from rest_framework.routers import DefaultRouter

from .views import CaptureTimeStampView

router = DefaultRouter()
router.register(r"anime", CaptureTimeStampView, basename="capture_timestamp")
urlpatterns = router.urls
