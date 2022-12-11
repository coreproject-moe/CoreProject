from uuid import UUID

from ninja import Schema


class LoginSchema(Schema):
    token: UUID
