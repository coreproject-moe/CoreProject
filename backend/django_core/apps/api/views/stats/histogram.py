

from apps.anime.models import AnimeModel
from apps.characters.models import CharacterModel
from apps.producers.models import ProducerModel
from apps.staffs.models import StaffModel
from django.db.models import Count
from django.db.models.functions import TruncMonth, TruncYear
from django.http.request import HttpRequest
from ninja import Router

from ...schemas.stats.histogram import HistogramSchema

router = Router()


# The database query is inspired from this stackoverflow thread
# https://stackoverflow.com/a/8746532


@router.get("/anime", response=list[HistogramSchema])
def anime_histogram(request: HttpRequest) -> list[AnimeModel]:
    query = (
        AnimeModel.objects.annotate(
            year=TruncYear("created_at"),
            month=TruncMonth("created_at"),
        )
        .values(
            "year",
            "month",
        )
        .annotate(
            count=Count("id"),
        )
        .order_by()
    )

    return query


@router.get("/character", response=list[HistogramSchema])
def character_histogram(request: HttpRequest) -> list[CharacterModel]:
    query = (
        CharacterModel.objects.annotate(
            year=TruncYear("created_at"),
            month=TruncMonth("created_at"),
        )
        .values(
            "year",
            "month",
        )
        .annotate(count=Count("id"))
        .order_by()
    )
    return query


@router.get("/staff", response=list[HistogramSchema])
def staff_histogram(request: HttpRequest) -> list[StaffModel]:
    query = (
        StaffModel.objects.annotate(
            year=TruncYear("created_at"),
            month=TruncMonth("created_at"),
        )
        .values(
            "year",
            "month",
        )
        .annotate(count=Count("id"))
        .order_by()
    )
    return query


@router.get("/producer", response=list[HistogramSchema])
def producer_histogram(request: HttpRequest) -> list[ProducerModel]:
    query = (
        ProducerModel.objects.annotate(
            year=TruncYear("created_at"),
            month=TruncMonth("created_at"),
        )
        .values(
            "year",
            "month",
        )
        .annotate(count=Count("id"))
        .order_by()
    )
    return query
