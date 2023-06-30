import strawberry
import strawberry_django
from apps.staffs.models import StaffModel, StaffAlternateNameModel

from ..filters.staff import StaffFilter


@strawberry.django.type(StaffAlternateNameModel)
class StaffAlternateName:
    name: str


@strawberry.django.type(StaffModel, filters=StaffFilter)
class Staff:
    mal_id: int
    kitsu_id: int
    anilist_id: int

    name: str
    given_name: str
    family_name: str
    alternate_names: StaffAlternateName

    character_image: str
    about: str
