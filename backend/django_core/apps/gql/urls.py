from django.urls import path

from strawberry.django.views import GraphQLView
from .schema import schema as schema
from .views import GraphQLView

urlpatterns = [
    path("", GraphQLView.as_view(schema=schema)),
]
