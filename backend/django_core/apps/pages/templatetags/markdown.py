import markdown as python_markdown
from django import template
from markdown.extensions.codehilite import CodeHiliteExtension

register = template.Library()


@register.filter(name="markdown")
def markdown(text: str):
    """Returns the value turned into a list."""
    x = python_markdown.markdown(
        text,
        extensions=[
            "fenced_code",
            CodeHiliteExtension(
                noclasses=True,
                pygments_style="github-dark",
                use_pygments=True,
            ),
        ],
    )
    print(x)
    return x
