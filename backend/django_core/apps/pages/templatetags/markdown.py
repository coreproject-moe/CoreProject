import markdown as python_markdown
from django import template
from pymdownx.highlight import HighlightExtension

register = template.Library()


@register.filter(name="markdown")
def markdown(text: str) -> str:
    """Returns the value turned into a list."""
    return python_markdown.markdown(
        text,
        extensions=[
            "pymdownx.superfences",
            "pymdownx.emoji",
            "pymdownx.escapeall",
            HighlightExtension(
                noclasses=True,
                pygments_style="github-dark",
                use_pygments=True,
            ),
        ],
    )
