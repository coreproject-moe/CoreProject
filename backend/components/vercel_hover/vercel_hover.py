import random
import sys

from django.core.cache import cache
from django_components import component


@component.register("vercel_hover")
class VercelHover(component.Component):
    template_name = "vercel_hover/vercel_hover.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(
        self,
        direction: str,
        duration: int = 200,
        glider_container_class: str | None = None,
        active_element_class: str | None = None,
    ):
        return {
            "duration": duration,
            "direction": direction,
            "glider_container_class": glider_container_class,
            "active_element_class": active_element_class,
        }
