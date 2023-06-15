from strawberry.django.views import AsyncGraphQLView
from .schema import schema
from django.urls import path

urlpatterns = [
    path("", AsyncGraphQLView.as_view(schema=schema)),
]
