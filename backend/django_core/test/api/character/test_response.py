from typing import NoReturn

from apps.characters.models import CharacterModel
from apps.user.models import CustomUser as User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class CharacterTestCases(APITestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.url = "/api/v2/character/"

    def setUp(self):
        self.character = CharacterModel.objects.create(
            mal_id=10,
            kitsu_id=10,
            anilist_id=10,
            name="Hello",
            name_kanji="world",
            about="Hello world",
        )
        # Create 2 users
        self.normal_user = User.objects.create_user(
            username="testuser#0001", email="admin2@django.com", password="testpassword"
        )
        self.normal_token = Token.objects.create(user=self.normal_user)

        self.super_user = User.objects.create_superuser(
            username="testuser1#0001", email="admin1@django.com", password="testpassword"
        )
        self.super_token = Token.objects.create(user=self.super_user)

    def tearDown(self) -> None:
        self.normal_token.delete()
        self.normal_user.delete()

        self.super_user.delete()
        self.super_token.delete()

        self.character.delete()

    def test_get_endpoint(self) -> NoReturn:
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Response looks okay")

        self.assertEqual(
            response.json(),
            [
                {
                    "mal_id": 10,
                    "kitsu_id": 10,
                    "anilist_id": 10,
                    "name": "Hello",
                    "name_kanji": "world",
                    "character_image": None,
                    "about": "Hello world",
                }
            ],
        )

    def test_post_endpoint(self) -> NoReturn:
        unauthenticated_response = self.client.post(
            self.url,
            {
                "mal_id": 11,
                "kitsu_id": 11,
                "anilist_id": 11,
                "name": "Hello w",
                "name_kanji": "o world",
                "character_image": None,
                "about": "Hello world 1",
            },
            format="json",
        )
        self.assertEqual(
            unauthenticated_response.status_code,
            status.HTTP_401_UNAUTHORIZED,
            "Unauthorized Response Status Code looks okay",
        )
        self.assertEqual(
            unauthenticated_response.json(),
            {"detail": "Authentication credentials were not provided."},
            "Unauthorized Response looks okay",
        )

        # Protected response
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.normal_token.key}")
        protected_response = self.client.post(
            self.url,
            {
                "mal_id": 111,
                "kitsu_id": 111,
                "anilist_id": 111,
                "name": "Hello wo",
                "name_kanji": "lo world",
                "character_image": None,
                "about": "Hello world 11",
            },
            format="json",
        )
        self.assertEqual(
            protected_response.status_code,
            status.HTTP_403_FORBIDDEN,
            "Protected Response Status Code looks okay",
        )
        self.assertEqual(
            protected_response.json(),
            {"detail": "You do not have permission to perform this action."},
            "Protected Response looks okay",
        )

        # Superuser test
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.super_token.key}")
        final_response = self.client.post(
            self.url,
            {
                "mal_id": 1111,
                "kitsu_id": 1111,
                "anilist_id": 1111,
                "name": "Hello wor",
                "name_kanji": "llo world",
                "character_image": None,
                "about": "Hello world 111",
            },
            format="json",
        )
        self.assertEqual(
            final_response.status_code,
            status.HTTP_201_CREATED,
            "Super Response Status Code looks okay",
        )
        self.assertEqual(
            final_response.json(),
            {
                "mal_id": 1111,
                "kitsu_id": 1111,
                "anilist_id": 1111,
                "name": "Hello wor",
                "name_kanji": "llo world",
                "character_image": None,
                "about": "Hello world 111",
            },
            "Super Response looks okay",
        )
        self.assertEqual(CharacterModel.objects.get(mal_id=1111).name, "Hello wor")
