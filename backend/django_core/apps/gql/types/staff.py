from apps.staffs.models import StaffAlternateNameModel, StaffModel
import strawberry_django

from ..filters.staff import StaffFilter


@strawberry_django.type(StaffAlternateNameModel)
class StaffAlternateNameType:
    name: str


@strawberry_django.type(StaffModel, filters=StaffFilter)
class StaffType:
    mal_id: int
    kitsu_id: int
    anilist_id: int

    name: str
    given_name: str
    family_name: str
    alternate_names: "StaffAlternateNameType"

    character_image: str
    about: str
