import pytest
from apps.api.urls import api
from apps.characters.models import CharacterModel
from django.test import TestCase
from ninja.testing import TestClient

client = TestClient(api.default_router)


@pytest.mark.database
class CharacterAPITestCase(TestCase):
    def setUp(self):
        CharacterModel.objects.create(
            id=1,
            mal_id=1,
            kitsu_id=1,
            anilist_id=1,
            name="Spike",
            name_kanji="スパイク・スピーゲル",
            about="""Birthdate: June 26, 2044\nHeight: 185 cm (6' 1")\nWeight: 70 kg (155 lbs)\nBlood type: O\nPlanet of Origin: Mars\n\nSpike Spiegel is a tall and lean 27-year-old bounty hunter born on Mars. The inspiration for Spike is found in martial artist Bruce Lee who uses the martial arts style of Jeet Kune Do as depicted in Session 8, "Waltz For Venus". He has fluffy, dark green hair (which is inspired by Yusaku Matsuda's) and reddish brown eyes, one of which is artificial and lighter than the other. He is usually dressed in a blue leisure suit, with a yellow shirt and Lupin III inspired boots. A flashback in Session 6 revealed it was his fully functioning right eye which was surgically replaced by the cybernetic one (although Spike himself may not have conscious recollection of the procedure since he claims to have lost his natural eye in an "accident"). One theory is that his natural eye may have been lost during the pre-series massacre in which he supposedly "died". The purpose of this cybernetic eye is never explicitly stated, though it apparently gives him exceptional hand-eye coordination - particularly with firearms (Spike's gun of choice is a Jericho 941, as seen throughout the series). In the first episode, when facing a bounty-head using Red Eye, Spike mocks him, calling his moves "too slow". At first, this seems like posturing on Spike's part, but even with his senses and reflexes accelerated to superhuman levels by the drug, the bounty cannot even touch Spike. A recurring device throughout the entire show is a closeup on Spike's fully-natural left eye before dissolving to a flashback of his life as part of the syndicate. As said by Spike himself in the last episode, his right eye "only sees the present" and his left eye "only sees the past." Spike often has a bent cigarette between his lips, sometimes despite rain or "No Smoking" signs.""",
        )

    def test_character_api_response_given_mal_id(self):
        res = self.client.get("/api/v1/characters", {"mal_id": 1})
        actual_data = res.json()
        actual_items = actual_data["items"][0]
        assert actual_items["mal_id"] == 1
        assert actual_items["kitsu_id"] == 1
        assert actual_items["anilist_id"] == 1
        assert actual_items["name"] == "Spike"
        assert (
            actual_items["about"]
            == """Birthdate: June 26, 2044\nHeight: 185 cm (6' 1")\nWeight: 70 kg (155 lbs)\nBlood type: O\nPlanet of Origin: Mars\n\nSpike Spiegel is a tall and lean 27-year-old bounty hunter born on Mars. The inspiration for Spike is found in martial artist Bruce Lee who uses the martial arts style of Jeet Kune Do as depicted in Session 8, "Waltz For Venus". He has fluffy, dark green hair (which is inspired by Yusaku Matsuda's) and reddish brown eyes, one of which is artificial and lighter than the other. He is usually dressed in a blue leisure suit, with a yellow shirt and Lupin III inspired boots. A flashback in Session 6 revealed it was his fully functioning right eye which was surgically replaced by the cybernetic one (although Spike himself may not have conscious recollection of the procedure since he claims to have lost his natural eye in an "accident"). One theory is that his natural eye may have been lost during the pre-series massacre in which he supposedly "died". The purpose of this cybernetic eye is never explicitly stated, though it apparently gives him exceptional hand-eye coordination - particularly with firearms (Spike's gun of choice is a Jericho 941, as seen throughout the series). In the first episode, when facing a bounty-head using Red Eye, Spike mocks him, calling his moves "too slow". At first, this seems like posturing on Spike's part, but even with his senses and reflexes accelerated to superhuman levels by the drug, the bounty cannot even touch Spike. A recurring device throughout the entire show is a closeup on Spike's fully-natural left eye before dissolving to a flashback of his life as part of the syndicate. As said by Spike himself in the last episode, his right eye "only sees the present" and his left eye "only sees the past." Spike often has a bent cigarette between his lips, sometimes despite rain or "No Smoking" signs."""
        )

    def test_character_api_response_given_kitsu_id(self):
        res = self.client.get("/api/v1/characters", {"kitsu_id": 1})
        actual_data = res.json()
        actual_items = actual_data["items"][0]
        assert actual_items["mal_id"] == 1
        assert actual_items["kitsu_id"] == 1
        assert actual_items["anilist_id"] == 1
        assert actual_items["name"] == "Spike"
        assert (
            actual_items["about"]
            == """Birthdate: June 26, 2044\nHeight: 185 cm (6' 1")\nWeight: 70 kg (155 lbs)\nBlood type: O\nPlanet of Origin: Mars\n\nSpike Spiegel is a tall and lean 27-year-old bounty hunter born on Mars. The inspiration for Spike is found in martial artist Bruce Lee who uses the martial arts style of Jeet Kune Do as depicted in Session 8, "Waltz For Venus". He has fluffy, dark green hair (which is inspired by Yusaku Matsuda's) and reddish brown eyes, one of which is artificial and lighter than the other. He is usually dressed in a blue leisure suit, with a yellow shirt and Lupin III inspired boots. A flashback in Session 6 revealed it was his fully functioning right eye which was surgically replaced by the cybernetic one (although Spike himself may not have conscious recollection of the procedure since he claims to have lost his natural eye in an "accident"). One theory is that his natural eye may have been lost during the pre-series massacre in which he supposedly "died". The purpose of this cybernetic eye is never explicitly stated, though it apparently gives him exceptional hand-eye coordination - particularly with firearms (Spike's gun of choice is a Jericho 941, as seen throughout the series). In the first episode, when facing a bounty-head using Red Eye, Spike mocks him, calling his moves "too slow". At first, this seems like posturing on Spike's part, but even with his senses and reflexes accelerated to superhuman levels by the drug, the bounty cannot even touch Spike. A recurring device throughout the entire show is a closeup on Spike's fully-natural left eye before dissolving to a flashback of his life as part of the syndicate. As said by Spike himself in the last episode, his right eye "only sees the present" and his left eye "only sees the past." Spike often has a bent cigarette between his lips, sometimes despite rain or "No Smoking" signs."""
        )

    def test_character_api_response_given_anilist_id(self):
        res = self.client.get("/api/v1/characters", {"anilist": 1})
        actual_data = res.json()
        actual_items = actual_data["items"][0]
        assert actual_items["mal_id"] == 1
        assert actual_items["kitsu_id"] == 1
        assert actual_items["anilist_id"] == 1
        assert actual_items["name"] == "Spike"
        assert (
            actual_items["about"]
            == """Birthdate: June 26, 2044\nHeight: 185 cm (6' 1")\nWeight: 70 kg (155 lbs)\nBlood type: O\nPlanet of Origin: Mars\n\nSpike Spiegel is a tall and lean 27-year-old bounty hunter born on Mars. The inspiration for Spike is found in martial artist Bruce Lee who uses the martial arts style of Jeet Kune Do as depicted in Session 8, "Waltz For Venus". He has fluffy, dark green hair (which is inspired by Yusaku Matsuda's) and reddish brown eyes, one of which is artificial and lighter than the other. He is usually dressed in a blue leisure suit, with a yellow shirt and Lupin III inspired boots. A flashback in Session 6 revealed it was his fully functioning right eye which was surgically replaced by the cybernetic one (although Spike himself may not have conscious recollection of the procedure since he claims to have lost his natural eye in an "accident"). One theory is that his natural eye may have been lost during the pre-series massacre in which he supposedly "died". The purpose of this cybernetic eye is never explicitly stated, though it apparently gives him exceptional hand-eye coordination - particularly with firearms (Spike's gun of choice is a Jericho 941, as seen throughout the series). In the first episode, when facing a bounty-head using Red Eye, Spike mocks him, calling his moves "too slow". At first, this seems like posturing on Spike's part, but even with his senses and reflexes accelerated to superhuman levels by the drug, the bounty cannot even touch Spike. A recurring device throughout the entire show is a closeup on Spike's fully-natural left eye before dissolving to a flashback of his life as part of the syndicate. As said by Spike himself in the last episode, his right eye "only sees the present" and his left eye "only sees the past." Spike often has a bent cigarette between his lips, sometimes despite rain or "No Smoking" signs."""
        )

    def test_character_api_response_given_name(self):
        res = self.client.get("/api/v1/characters", {"name": "Spike"})
        actual_data = res.json()
        actual_items = actual_data["items"][0]
        assert actual_items["mal_id"] == 1
        assert actual_items["kitsu_id"] == 1
        assert actual_items["anilist_id"] == 1
        assert actual_items["name"] == "Spike"
        assert (
            actual_items["about"]
            == """Birthdate: June 26, 2044\nHeight: 185 cm (6' 1")\nWeight: 70 kg (155 lbs)\nBlood type: O\nPlanet of Origin: Mars\n\nSpike Spiegel is a tall and lean 27-year-old bounty hunter born on Mars. The inspiration for Spike is found in martial artist Bruce Lee who uses the martial arts style of Jeet Kune Do as depicted in Session 8, "Waltz For Venus". He has fluffy, dark green hair (which is inspired by Yusaku Matsuda's) and reddish brown eyes, one of which is artificial and lighter than the other. He is usually dressed in a blue leisure suit, with a yellow shirt and Lupin III inspired boots. A flashback in Session 6 revealed it was his fully functioning right eye which was surgically replaced by the cybernetic one (although Spike himself may not have conscious recollection of the procedure since he claims to have lost his natural eye in an "accident"). One theory is that his natural eye may have been lost during the pre-series massacre in which he supposedly "died". The purpose of this cybernetic eye is never explicitly stated, though it apparently gives him exceptional hand-eye coordination - particularly with firearms (Spike's gun of choice is a Jericho 941, as seen throughout the series). In the first episode, when facing a bounty-head using Red Eye, Spike mocks him, calling his moves "too slow". At first, this seems like posturing on Spike's part, but even with his senses and reflexes accelerated to superhuman levels by the drug, the bounty cannot even touch Spike. A recurring device throughout the entire show is a closeup on Spike's fully-natural left eye before dissolving to a flashback of his life as part of the syndicate. As said by Spike himself in the last episode, his right eye "only sees the present" and his left eye "only sees the past." Spike often has a bent cigarette between his lips, sometimes despite rain or "No Smoking" signs."""
        )

    def test_character_api_response_given_kanji_name(self):
        res = self.client.get("/api/v1/characters", {"name": "スパイク・スピーゲル"})
        actual_data = res.json()
        actual_items = actual_data["items"][0]
        assert actual_items["mal_id"] == 1
        assert actual_items["kitsu_id"] == 1
        assert actual_items["anilist_id"] == 1
        assert actual_items["name"] == "Spike"
        assert (
            actual_items["about"]
            == """Birthdate: June 26, 2044\nHeight: 185 cm (6' 1")\nWeight: 70 kg (155 lbs)\nBlood type: O\nPlanet of Origin: Mars\n\nSpike Spiegel is a tall and lean 27-year-old bounty hunter born on Mars. The inspiration for Spike is found in martial artist Bruce Lee who uses the martial arts style of Jeet Kune Do as depicted in Session 8, "Waltz For Venus". He has fluffy, dark green hair (which is inspired by Yusaku Matsuda's) and reddish brown eyes, one of which is artificial and lighter than the other. He is usually dressed in a blue leisure suit, with a yellow shirt and Lupin III inspired boots. A flashback in Session 6 revealed it was his fully functioning right eye which was surgically replaced by the cybernetic one (although Spike himself may not have conscious recollection of the procedure since he claims to have lost his natural eye in an "accident"). One theory is that his natural eye may have been lost during the pre-series massacre in which he supposedly "died". The purpose of this cybernetic eye is never explicitly stated, though it apparently gives him exceptional hand-eye coordination - particularly with firearms (Spike's gun of choice is a Jericho 941, as seen throughout the series). In the first episode, when facing a bounty-head using Red Eye, Spike mocks him, calling his moves "too slow". At first, this seems like posturing on Spike's part, but even with his senses and reflexes accelerated to superhuman levels by the drug, the bounty cannot even touch Spike. A recurring device throughout the entire show is a closeup on Spike's fully-natural left eye before dissolving to a flashback of his life as part of the syndicate. As said by Spike himself in the last episode, his right eye "only sees the present" and his left eye "only sees the past." Spike often has a bent cigarette between his lips, sometimes despite rain or "No Smoking" signs."""
        )

    def test_character_api_response_given_individual_url(self):
        res = self.client.get("/api/v1/characters/1/")
        actual_data = res.json()
        assert actual_data["mal_id"] == 1
        assert actual_data["kitsu_id"] == 1
        assert actual_data["anilist_id"] == 1
        assert actual_data["name"] == "Spike"
        assert (
            actual_data["about"]
            == """Birthdate: June 26, 2044\nHeight: 185 cm (6' 1")\nWeight: 70 kg (155 lbs)\nBlood type: O\nPlanet of Origin: Mars\n\nSpike Spiegel is a tall and lean 27-year-old bounty hunter born on Mars. The inspiration for Spike is found in martial artist Bruce Lee who uses the martial arts style of Jeet Kune Do as depicted in Session 8, "Waltz For Venus". He has fluffy, dark green hair (which is inspired by Yusaku Matsuda's) and reddish brown eyes, one of which is artificial and lighter than the other. He is usually dressed in a blue leisure suit, with a yellow shirt and Lupin III inspired boots. A flashback in Session 6 revealed it was his fully functioning right eye which was surgically replaced by the cybernetic one (although Spike himself may not have conscious recollection of the procedure since he claims to have lost his natural eye in an "accident"). One theory is that his natural eye may have been lost during the pre-series massacre in which he supposedly "died". The purpose of this cybernetic eye is never explicitly stated, though it apparently gives him exceptional hand-eye coordination - particularly with firearms (Spike's gun of choice is a Jericho 941, as seen throughout the series). In the first episode, when facing a bounty-head using Red Eye, Spike mocks him, calling his moves "too slow". At first, this seems like posturing on Spike's part, but even with his senses and reflexes accelerated to superhuman levels by the drug, the bounty cannot even touch Spike. A recurring device throughout the entire show is a closeup on Spike's fully-natural left eye before dissolving to a flashback of his life as part of the syndicate. As said by Spike himself in the last episode, his right eye "only sees the present" and his left eye "only sees the past." Spike often has a bent cigarette between his lips, sometimes despite rain or "No Smoking" signs."""
        )
