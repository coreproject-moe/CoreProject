# models.py
from sqlalchemy import (
    Column,
    BigInteger,
    String,
    UniqueConstraint,
    Integer,
    Date,
    PickleType,
)
from ._base import Base


class Staff(Base):
    __tablename__ = "staff"

    id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True)
    mal_id = Column(BigInteger, nullable=False)
    name = Column(String, nullable=True)
    given_name = Column(String, nullable=True)
    family_name = Column(String, nullable=True)
    alternate_name = Column(PickleType, nullable=True)
    birthday = Column(Date, nullable=True)

    __table_args__ = (
        UniqueConstraint("mal_id", "name", "given_name", "family_name", name="_name_uc"),
    )
