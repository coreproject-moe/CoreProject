import datetime

from ninja.schema import Schema


class HistogramSchema(Schema):
    year: datetime.datetime
    month: datetime.datetime
    count: int
