from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from hashlib import md5

# tests.py
class SimpleTest(TestCase):
    def __init__(self) -> None:
        self.client = Client()

    def setUp(self):
        __User: User = get_user_model()
        self.user = __User.objects.create_user(
            username="example", email="someone@example.com", password="upCiAc5os3586K"
        )
        self.client.login(username="example", password="upCiAc5os3586K")

    def tearDown(self) -> None:
        self.user.delete()

    def test_api_response(self) -> None:
        self.client.get(reverse("api_avatar", kwargs={"user_id": self.user.id}))
