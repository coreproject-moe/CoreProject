from rest_framework.routers import DefaultRouter

from .views import CaptureVolumeView

router = DefaultRouter()
router.register(r"volume", CaptureVolumeView, basename="capture_volume")
urlpatterns = router.urls
