from django.db.models import Q, QuerySet
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import File, Form, Query, Router
from ninja.files import UploadedFile
from ninja.pagination import paginate

from ....staffs.models import StaffAlternateNameModel, StaffModel
from ...filters.staffs import StaffFilter
from ...schemas.staffs import StaffSchema

router = Router()


@router.get("", response=list[StaffSchema])
@paginate
def get_staff_info(
    request: HttpRequest,
    filters: StaffFilter = Query(...),
) -> QuerySet[StaffModel]:
    query_object = Q()
    query_dict = filters.dict(exclude_none=True)

    staff_name = query_dict.pop("name", None)
    if staff_name:
        _query_ = Q()
        # Modify this
        for position in staff_name.split(","):
            _query_ |= Q(**{"name__icontains": position.strip()}) | Q(
                **{"alternate_names__name__icontains": position.strip()}
            )
        query_object &= _query_

    # Specilized lookups
    specialized_name_lookups = [
        "given_name",
        "family_name",
    ]
    for specialized_name in specialized_name_lookups:
        value = query_dict.pop(specialized_name, None)
        if value:
            _query_ = Q()
            for position in value.split(","):
                _query_ |= Q(**{f"{specialized_name}__icontains": int(position.strip())})
            query_object &= _query_

    # Specialized lookups but with ids
    id_lookups = [
        "mal_id",
        "kitsu_id",
        "anilist_id",
    ]
    for id in id_lookups:
        value = query_dict.pop(id, None)
        if value:
            _query_ = Q()
            for position in value.split(","):
                _query_ |= Q(**{f"{id}": int(position.strip())})
            query_object &= _query_

    query = StaffModel.objects.all()

    if query_object:
        query = query.filter(query_object).distinct()

    return query


@router.post("", response=StaffSchema)
def post_staff_info(
    request,
    mal_id: int | None = Form(default=None),
    kitsu_id: int | None = Form(default=None),
    anilist_id: int | None = Form(default=None),
    name: str = Form(..., max_length=1024),
    given_name: str | None = Form(default=None, max_length=1024),
    family_name: str | None = Form(default=None, max_length=1024),
    staff_image: UploadedFile | None = File(default=None),
    about: str | None = Form(default=None),
    alternate_names: list[str] = Form(default=None),
):
    kwargs = {
        "mal_id": mal_id,
        "kitsu_id": kitsu_id,
        "anilist_id": anilist_id,
        "name": name,
        "given_name": given_name,
        "family_name": family_name,
        "staff_image": staff_image,
        "about": about,
        "alternate_names": alternate_names,
    }

    model_data = {
        key: value
        for key, value in kwargs.items()
        if key
        not in [
            # Ignore M2M relations
            "alternate_names",
        ]
        and value
        not in [
            None,
            "",  # ignore empty strings
            0,
        ]
    }
    staff_model_instance, _ = StaffModel.objects.get_or_create(
        name=kwargs["name"],
        defaults=model_data,
    )

    if alternate_names_list := kwargs.get("alternate_names", None):
        for alternate_name in alternate_names_list[0].split(","):
            anime_synonym_instance, _ = StaffAlternateNameModel.objects.get_or_create(
                name=alternate_name
            )
            staff_model_instance.alternate_names.add(anime_synonym_instance)

    return staff_model_instance


@router.get("/{str:staff_id}/", response=StaffSchema)
def get_individual_staff_info(
    request: HttpRequest,
    staff_id: str,
):
    queryset = get_object_or_404(StaffModel, id=staff_id)
    return queryset
