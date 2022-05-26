from apps.anime.views.anime_producer import AnimeProducerView
from django.urls import include, path
from rest_framework_nested import routers

from .views.anime_info import AnimeInfoView

router = routers.SimpleRouter()
router.register(r"anime", AnimeInfoView, basename="anime_info")

base_router = routers.NestedSimpleRouter(router, r"anime", lookup="anime")
base_router.register(r"producers", AnimeProducerView, basename="anime_producers")


# https://stackoverflow.com/questions/51823331/django-rest-framework-define-extra-arguments-using-the-action-decorator
urlpatterns = [
    path("", include(router.urls)),
    path("", include(base_router.urls)),
]
