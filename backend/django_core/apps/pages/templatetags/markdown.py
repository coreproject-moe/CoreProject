from django import template
import markdown as python_markdown

register = template.Library()


@register.filter(name="markdown")
def markdown(text: str):
    """Returns the value turned into a list."""
    return python_markdown.markdown(text)
