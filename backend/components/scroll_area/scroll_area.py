import random
import sys

from django.core.cache import cache
from django_components import component


def get_random_integer():
    random_integer = random.randint(0, sys.maxsize)

    if cache.get("scroll_area") == random_integer:
        get_random_integer()
    else:
        cache.set("scroll_area", random_integer, 1)
        return random_integer


@component.register("scroll_area")
class ScollArea(component.Component):
    template_name = "scroll_area/scroll_area.html"

    def get_context_data(
        self,
        scroll_area_class: str,
        parent_class: str,
        offset_scrollbar: str | None = None,
    ):
        return {
            "class": scroll_area_class,
            "parent_class": parent_class,
            "offset_scrollbar": offset_scrollbar,
            "random_integer": get_random_integer(),
        }

    # class Media:
    #     js = "scroll_area/scroll_area.js"
