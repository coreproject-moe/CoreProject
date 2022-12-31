from ninja import Schema


class LoginSchema(Schema):
    token: str
