from django.urls import path

from .schema import schema as schema
from .views import GraphQLView

urlpatterns = [
    path("", GraphQLView.as_view(schema=schema)),
]
