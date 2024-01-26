from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpRequest
from ...serializers.upload.doodstream import ProviderSerializer
from rest_framework import generics
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
import requests


class DoodstreamAPIView(generics.CreateAPIView):
    serializer_class = ProviderSerializer

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            url = f"https://doodapi.com/api/upload/server?key={serializer.validated_data['api_key']}"
            res = requests.get(url)

            return Response(status=200, data={"url": res.json()["result"]})
        except:
            return Response(status=504)
