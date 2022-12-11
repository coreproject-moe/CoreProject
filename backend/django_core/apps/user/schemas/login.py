from ninja import Schema
from uuid import UUID


class LoginSchema(Schema):
    token: UUID
