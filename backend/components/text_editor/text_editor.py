from django_components import component


@component.register("text_editor")
class TextEditor(component.Component):
    template_name = "text_editor/text_editor.html"

    class Media:
        css = "text_editor/text_editor.css"