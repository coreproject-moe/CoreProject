from ninja import Router
from apps.anime.models import AnimeModel
import pandas as pd
import json

router = Router()


@router.get("/anime")
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

    # We want custom datastructure.
    # {
    #   2023: {
    # }
    # }

    # returnable_dictionary: dict[int, dict[int, dict[str, int]]] = {}

    return json.loads(histogram_json)
