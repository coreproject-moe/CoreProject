from ninja import File, Form, Query, Router
from ninja.files import UploadedFile
from ninja.pagination import paginate

from django.db.models import Q, QuerySet
from django.db.models.functions import Greatest
from django.http import Http404, HttpRequest
from django.shortcuts import get_object_or_404

from ....staffs.models import StaffAlternateNameModel, StaffModel
from ...filters.staffs import StaffFilter
from ...schemas.staffs import StaffSchema

try:
    from django.contrib.postgres.search import TrigramSimilarity

    HAS_POSTGRES = True
except ImportError:
    HAS_POSTGRES = False

router = Router()


@router.get("", response=list[StaffSchema])
@paginate
def get_staff_info(
    request: HttpRequest,
    filters: StaffFilter = Query(...),
) -> QuerySet[StaffModel]:
    if not HAS_POSTGRES:
        raise Http404("Looksups are not supported on any other databases except Postgres")

    query_dict = filters.dict(exclude_none=True)

    query_object = Q()
    query = StaffModel.objects.all()

    staff_name = query_dict.pop("name", None)
    if staff_name:
        # Modify this
        query = (
            query.annotate(
                similiarity=Greatest(
                    TrigramSimilarity("name", staff_name),
                    TrigramSimilarity("alternate_names__name", staff_name),
                    TrigramSimilarity("family_name", staff_name),
                    TrigramSimilarity("given_name", staff_name),
                )
            )
            .filter(
                similiarity__gte=0.3,
            )
            .order_by("-similiarity")
        )

    # Specilized lookups
    for specialized_name in [
        "given_name",
        "family_name",
    ]:
        if value := query_dict.pop(specialized_name, None):
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
        if value := query_dict.pop(id, None):
            _query_ = Q()
            for position in value.split(","):
                _query_ |= Q(**{f"{id}": int(position.strip())})
            query_object &= _query_

    if query_object:
        query = query.filter(query_object).distinct()

    return query


@router.post("", response=StaffSchema)
def post_staff_info(
    request: HttpRequest,
    mal_id: int | None = Form(default=None),
    kitsu_id: int | None = Form(default=None),
    anilist_id: int | None = Form(default=None),
    name: str = Form(..., max_length=1024),
    given_name: str | None = Form(default=None, max_length=1024),
    family_name: str | None = Form(default=None, max_length=1024),
    staff_image: UploadedFile | None = File(default=None),
    about: str | None = Form(default=None),
    alternate_names: list[str] = Form(default=None),
) -> StaffModel:
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
        if key
        not in [
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
        for alternate_name in alternate_names_list:
            anime_synonym_instance = StaffAlternateNameModel.objects.create(
                name=alternate_name.strip(),
            )
            staff_model_instance.alternate_names.add(anime_synonym_instance)

    return staff_model_instance


@router.get("/{str:staff_id}/", response=StaffSchema)
def get_individual_staff_info(
    request: HttpRequest,
    staff_id: str,
) -> StaffModel:
    queryset = get_object_or_404(StaffModel, pk=staff_id)
    return queryset
