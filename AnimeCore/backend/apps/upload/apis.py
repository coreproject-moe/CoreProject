from rest_framework.routers import DefaultRouter

from .views import AnimeInfoView

router = DefaultRouter()
router.register(r"anime", AnimeInfoView, basename="anime_info")
urlpatterns = router.urls
