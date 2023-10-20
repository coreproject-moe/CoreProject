from django_components import component


@component.register("vercel_hover")
class VercelHover(component.Component):
    template_name = "vercel_hover/vercel_hover.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(
        self,
        direction: str,
        duration: int = 200,
        alpine: str | None = None,
        glider_container_class: str | None = None,
        active_element_class: str | None = None,
    ):
        return {
            "alpine": alpine,
            "duration": duration,
            "direction": direction,
            "glider_container_class": glider_container_class,
            "active_element_class": active_element_class,
        }

    class Media:
        css = "vercel_hover/vercel_hover.css"
        js = "vercel_hover/vercel_hover.js"
