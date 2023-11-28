import functools
import re

from django.conf import settings
from django.contrib.admindocs.views import simplify_regex
from django.core.exceptions import ViewDoesNotExist
from django.http.request import HttpRequest
from django.urls import URLPattern, URLResolver  # type: ignore


class RegexURLPattern:  # type: ignore
    pass


class RegexURLResolver:  # type: ignore
    pass


def describe_pattern(p):
    return str(p.pattern)


def extract_views_from_urlpatterns(urlpatterns, base="", namespace=None):
    """
    Return a list of views from a list of urlpatterns.

    Each object in the returned list is a three-tuple: (view_func, regex, name)
    """
    views = []
    for p in urlpatterns:
        if isinstance(p, (URLPattern, RegexURLPattern)):
            try:
                if not p.name:
                    name = p.name
                elif namespace:
                    name = f"{namespace}:{p.name}"
                else:
                    name = p.name
                pattern = describe_pattern(p)
                views.append((p.callback, base + pattern, name))
            except ViewDoesNotExist:
                continue
        elif isinstance(p, (URLResolver, RegexURLResolver)):
            try:
                patterns = p.url_patterns
            except ImportError:
                continue
            if namespace and p.namespace:
                _namespace = f"{namespace}:{p.namespace}"
            else:
                _namespace = p.namespace or namespace
            pattern = describe_pattern(p)

            views.extend(
                extract_views_from_urlpatterns(
                    patterns, base + pattern, namespace=_namespace
                )
            )
        elif hasattr(p, "_get_callback"):
            try:
                views.append((p._get_callback(), base + describe_pattern(p), p.name))
            except ViewDoesNotExist:
                continue
        elif hasattr(p, "url_patterns") or hasattr(p, "_get_url_patterns"):
            try:
                patterns = p.url_patterns
            except ImportError:
                continue
            views.extend(
                extract_views_from_urlpatterns(
                    patterns, base + describe_pattern(p), namespace=namespace
                )
            )
        else:
            raise TypeError(f"{p} does not appear to be a urlpattern object")
    return views


def urls(request: HttpRequest):
    urlpatterns = []
    urlconf = __import__(getattr(request, "urlconf", settings.ROOT_URLCONF), {}, {}, [""])
    view_functions = extract_views_from_urlpatterns(urlconf.urlpatterns)

    for func, regex, url_name in view_functions:
        if isinstance(func, functools.partial):
            func = func.func

        if hasattr(func, "view_class"):
            func = func.view_class

        url_name = url_name or ""
        url = simplify_regex(regex)

        admin_pattern = re.compile(r"^/admin(?:/|$)")
        if not admin_pattern.match(url):
            urlpatterns.append({"url": url, "name": url_name})

    return {"urlpatterns": urlpatterns}
