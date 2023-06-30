from ninja import Schema


class UsernameValiditySchema(Schema):
    status: int
    message: str
