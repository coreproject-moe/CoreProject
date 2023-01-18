from ninja import File, Form, Query, Router
from ninja.files import UploadedFile
from ninja.pagination import paginate

from django.db.models import Q, QuerySet
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from ....staffs.models import StaffModel
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
                **{"alternate_names__icontains": position.strip()}
            )
        query_object &= _query_

    # Specilized lookups
    for specialized_name in [
        "given_name",
        "family_name",
    ]:
        value = query_dict.pop(specialized_name, None)
        if value:
            _query_ = Q()
            for position in value.split(","):
                _query_ |= Q(**{f"{specialized_name}__icontains": int(position.strip())})
            query_object &= _query_

    # Specialized lookups but with ids
    for id in [
        "mal_id",
        "kitsu_id",
        "anilist_id",
    ]:
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
        #   Alternate names can be
        #       like this   :   ['hello,world']
        #   What we want is :   ['hello', 'world']
        "alternate_names": alternate_names[0].split(",") if alternate_names else None,
    }

    model_data = {
        key: value
        for key, value in kwargs.items()
        if value
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

    return staff_model_instance


@router.get("/{str:staff_id}/", response=StaffSchema)
def get_individual_staff_info(
    request: HttpRequest,
    staff_id: str,
):
    queryset = get_object_or_404(StaffModel, pk=staff_id)
    return queryset
