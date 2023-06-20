from ninja.schema import Schema
import datetime


class HistogramSchema(Schema):
    year: datetime.datetime
    month: datetime.datetime
    count: int
