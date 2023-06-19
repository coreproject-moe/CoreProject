from ninja import Router
from apps.anime.models import AnimeModel
import pandas as pd
from django.http.request import HttpRequest

router = Router()


@router.get("/anime", response=dict[int, dict[int, dict[str, int]]])
def anime_histogram(request):
    date_objects = AnimeModel.objects.all().values_list("created_at")
    pd_dataframe = pd.DataFrame(date_objects, columns=["created_at"])
    pd_dataframe["created_at"] = pd.to_datetime(pd_dataframe["created_at"])

    # Year and month
    pd_dataframe["month"] = pd_dataframe["created_at"].dt.month
    pd_dataframe["year"] = pd_dataframe["created_at"].dt.year

    histogram_data = (
        pd_dataframe.groupby(["month", "year"]).size().reset_index(name="count")
    )
    histogram_json = histogram_data.to_dict(
        orient="records"
    )  # [{"month": 6, "year": 2023, "count": 1}]

    returnable_dictionary: dict[int, dict[int, dict[str, int]]] = {}
    for item in histogram_json:
        year = item["year"]
        month = item["month"]
        count = item["count"]

        returnable_dictionary.setdefault(year, {})
        returnable_dictionary[year].setdefault(month, {"count": count})

    return returnable_dictionary


@router.get("/character", response=dict[int, dict[int, dict[str, int]]])
def character_histogram(request: HttpRequest):
    date_objects = AnimeModel.objects.all().values_list("created_at")
    pd_dataframe = pd.DataFrame(date_objects, columns=["created_at"])
    pd_dataframe["created_at"] = pd.to_datetime(pd_dataframe["created_at"])

    # Year and month
    pd_dataframe["month"] = pd_dataframe["created_at"].dt.month
    pd_dataframe["year"] = pd_dataframe["created_at"].dt.year

    histogram_data = (
        pd_dataframe.groupby(["month", "year"]).size().reset_index(name="count")
    )
    histogram_json = histogram_data.to_dict(
        orient="records"
    )  # [{"month": 6, "year": 2023, "count": 1}]

    returnable_dictionary: dict[int, dict[int, dict[str, int]]] = {}
    for item in histogram_json:
        year = item["year"]
        month = item["month"]
        count = item["count"]

        returnable_dictionary.setdefault(year, {})
        returnable_dictionary[year].setdefault(month, {"count": count})

    return returnable_dictionary
