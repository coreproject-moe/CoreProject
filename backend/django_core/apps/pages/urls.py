from django.urls import  path
from .views.stack import stack_view

urlpatterns = [
   path("stack/", stack_view, name="stack_view"),
]