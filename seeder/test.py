from shinobi.parser.character import CharacterParser
from shinobi.utilities.session import session

res = session.get("https://myanimelist.net/character/1")


# noqa: E501
parser = CharacterParser(res.text)
data = parser.build_dictionary()

print(data)
