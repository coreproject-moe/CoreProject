
from django_components import component


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
        }

    # class Media:
    #     js = "scroll_area/scroll_area.js"
