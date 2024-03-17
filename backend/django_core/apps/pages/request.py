from django.http import HttpRequest
from django_htmx.middleware import HtmxDetails

# https://github.com/adamchainz/django-htmx/blob/a08750cb67943b8d49322e3226e6c7f62eff07bc/example/example/views.py#L19-L22


# Typing pattern recommended by django-stubs:
# https://github.com/typeddjango/django-stubs#how-can-i-create-a-httprequest-thats-guaranteed-to-have-an-authenticated-user
class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails
