from django.http import HttpResponse
import bencodepy


class BencodeResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        data = bencodepy.bencode(data)
        super().__init__(content=data, **kwargs)
