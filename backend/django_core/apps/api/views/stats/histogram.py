from typing import Literal

import pandas as pd
from apps.anime.models import AnimeModel
from apps.characters.models import CharacterModel
from apps.producers.models import ProducerModel
from apps.staffs.models import StaffModel
from django.http.request import HttpRequest
from ninja import Router

router = Router()


# Types
RETURN_TYPE = dict[
    int,
    dict[
        Literal[1]
        | Literal[2]
        | Literal[3]
        | Literal[4]
        | Literal[5]
        | Literal[6]
        | Literal[7]
        | Literal[8]
        | Literal[9]
        | Literal[10]
        | Literal[11]
        | Literal[12],
        dict[Literal["count"], int],
    ],
]


def get_json_data_given_model(
    model: AnimeModel | CharacterModel | ProducerModel | StaffModel,
) -> RETURN_TYPE:
    date_objects = model.objects.all().values_list("created_at")
    pd_dataframe = pd.DataFrame(date_objects, columns=["created_at"])
    pd_dataframe["created_at"] = pd.to_datetime(pd_dataframe["created_at"])

    # Year and month
    pd_dataframe["month"] = pd_dataframe["created_at"].dt.month
    pd_dataframe["year"] = pd_dataframe["created_at"].dt.year

    histogram_data = (
        pd_dataframe.groupby(["month", "year"]).size().reset_index(name="count")
    )
    # [{"month": 6, "year": 2023, "count": 1}]
    histogram_json = histogram_data.to_dict(orient="records")

    return_data: RETURN_TYPE = {}
    for item in histogram_json:
        year = item["year"]
        month = item["month"]
        count = item["count"]

        return_data.setdefault(year, {})
        return_data[year].setdefault(month, {"count": count})

    return return_data


@router.get("/anime", response=RETURN_TYPE)
def anime_histogram(request: HttpRequest) -> RETURN_TYPE:
    return get_json_data_given_model(AnimeModel)


@router.get("/character", response=RETURN_TYPE)
def character_histogram(request: HttpRequest) -> RETURN_TYPE:
    return get_json_data_given_model(CharacterModel)


@router.get("/staff", response=dict[int, RETURN_TYPE])
def staff_histogram(request: HttpRequest) -> dict[int, RETURN_TYPE]:
    return get_json_data_given_model(StaffModel)


@router.get("/producer", response=dict[int, RETURN_TYPE])
def producer_histogram(request: HttpRequest) -> dict[int, RETURN_TYPE]:
    return get_json_data_given_model(ProducerModel)
