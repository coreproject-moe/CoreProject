from django_components import component
import random

@component.register("scroll_area")
class ScollArea(component.Component):
    template_name = "scroll_area/scroll_area.html"

    # get params
    def get_context_data(
        self,
        scroll_area_class: str,
        parent_class: str,
        offset_scrollbar: str | None = None,
    ):
        random_integer = random.randint(0,1_00_00_00_00_000)
        return {
            "class": scroll_area_class,
            "parent_class": parent_class,
            "offset_scrollbar": offset_scrollbar,
            "random_integer":random_integer
        }

    # class Media:
    #     js = "scroll_area/scroll_area.js"
