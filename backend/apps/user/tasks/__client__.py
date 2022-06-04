from http import client
import httpx

client = httpx.Client(http2=True)
