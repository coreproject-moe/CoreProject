import re
from urllib.parse import urlparse


def make_absolute_location(base_url, location):
    """
    Convert a location header into an absolute URL.
    """
    absolute_pattern = re.compile(r"^[a-zA-Z]+://.*$")
    if absolute_pattern.match(location):
        return location

    parsed_url = urlparse(base_url)

    if location.startswith("//"):
        # scheme relative
        return parsed_url.scheme + ":" + location

    elif location.startswith("/"):
        # host relative
        return parsed_url.scheme + "://" + parsed_url.netloc + location

    else:
        # path relative
        return (
            parsed_url.scheme
            + "://"
            + parsed_url.netloc
            + parsed_url.path.rsplit("/", 1)[0]
            + "/"
            + location
        )

    return location
