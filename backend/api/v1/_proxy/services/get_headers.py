def get_headers(environ):
    """
    Retrieve the HTTP headers from a WSGI environment dictionary.  See
    https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpRequest.META
    """
    headers = {}
    for key, value in environ.items():
        # Sometimes, things don't like when you send the requesting host through.
        if key.startswith("HTTP_") and key != "HTTP_HOST":
            headers[key[5:].replace("_", "-")] = value
        elif key in ("CONTENT_TYPE", "CONTENT_LENGTH"):
            headers[key.replace("_", "-")] = value

    return headers
