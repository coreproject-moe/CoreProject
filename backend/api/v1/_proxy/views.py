# https://github.com/mjumbewu/django-proxy/blob/master/proxy/views.py

from django.http import HttpResponse
from django.http import QueryDict

from platform import python_version

import requests


from .services.get_headers import get_headers
from .services.make_absolute_location import make_absolute_location


def proxy_view(request, url, requests_args=None):
    """
    Forward as close to an exact copy of the request as possible along to the
    given url.  Respond with as close to an exact copy of the resulting
    response as possible.

    If there are any additional arguments you wish to send to requests, put
    them in the requests_args dictionary.
    """
    requests_args = (requests_args or {}).copy()
    headers = get_headers(request.META)
    params = request.GET.copy()

    if "headers" not in requests_args:
        requests_args["headers"] = {}
    if "data" not in requests_args:
        requests_args["data"] = request.body
    if "params" not in requests_args:
        requests_args["params"] = QueryDict("", mutable=True)

    # Overwrite any headers and params from the incoming request with explicitly
    # specified values for the requests library.
    headers.update(requests_args["headers"])
    params.update(requests_args["params"])

    # If there's a content-length header from Django, it's probably in all-caps
    # and requests might not notice it, so just remove it.
    for key in list(headers.keys()):
        if key.lower() == "content-length":
            del headers[key]

    requests_args["headers"] = headers
    requests_args["params"] = params

    response = requests.request(request.method, url, **requests_args)

    proxy_response = HttpResponse(
        response.content,
        status=response.status_code,
        headers={
            "server": f"Python/{python_version()} Requests/{requests.__version__}",
        },
    )

    excluded_headers = set(
        [
            # Hop-by-hop headers
            # ------------------
            # Certain response headers should NOT be just tunneled through.  These
            # are they.  For more info, see:
            # http://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html#sec13.5.1
            "connection",
            "keep-alive",
            "proxy-authenticate",
            "proxy-authorization",
            "te",
            "trailers",
            "transfer-encoding",
            "upgrade",
            # We dont want the origin server url
            "server",
            # Although content-encoding is not listed among the hop-by-hop headers,
            # it can cause trouble as well.  Just let the server set the value as
            # it should be.
            "content-encoding",
            # Since the remote server may or may not have sent the content in the
            # same encoding as Django will, let Django worry about what the length
            # should be.
            "content-length",
        ]
    )
    for key, value in response.headers.items():
        if key.lower() in excluded_headers:
            continue
        elif key.lower() == "location":
            # If the location is relative at all, we want it to be absolute to
            # the upstream server.
            proxy_response[key] = make_absolute_location(response.url, value)
        else:
            proxy_response[key] = value

    return proxy_response
