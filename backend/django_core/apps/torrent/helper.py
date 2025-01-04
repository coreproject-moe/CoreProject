import re
from django.http import HttpRequest, Http404


def get_params(request: HttpRequest):
    url_string = request.META["QUERY_STRING"]
    params: dict[str, str | int] = {}

    pattern = re.compile(r"([^&=]+)=([^&=]+)")
    matches = pattern.findall(url_string)

    if not matches:
        raise Http404("No valid parameters found in URL.")

    for key, value in matches:
        params[key] = value

    return params
