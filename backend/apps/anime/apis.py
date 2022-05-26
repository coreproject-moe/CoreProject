from django.urls import include, path
from rest_framework_nested import routers

from .views.anime_info import AnimeInfoView

router = routers.SimpleRouter()
router.register(r"anime", AnimeInfoView, basename="anime_info")
# https://stackoverflow.com/questions/51823331/django-rest-framework-define-extra-arguments-using-the-action-decorator
urlpatterns = [
    path("", include(router.urls)),
]
