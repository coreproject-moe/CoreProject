import requests

from shinobi.parser.staff import StaffParser
from shinobi.utilities.session import session


from src.seeder_flet.models._engine import Session
from src.seeder_flet.models._models import Staff


def get_staff_res_given_mal_id(mal_id: int) -> requests.Response:
    return session.get(f"https://myanimelist.net/people/{mal_id}")


# noqa: E501
res = get_staff_res_given_mal_id(1)
parser = StaffParser(res.text)
data = parser.build_dictionary()

for i in data:
    with Session() as _session:
        db = Staff(mal_id=i)
        _session.add(db)
        _session.commit()
