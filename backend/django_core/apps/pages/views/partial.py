from ..request import HtmxHttpRequest
from django.http import HttpResponse
from django.shortcuts import render

import markdown as python_markdown
from pymdownx.highlight import HighlightExtension


async def markdown_endpoint(request: "HtmxHttpRequest") -> "HttpResponse":
    python_markdown.markdown(
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
    return render(
        request,
        "partials/markdown.html",
        context={
            "markdown": "world",
        },
    )
