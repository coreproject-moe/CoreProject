# models.py
from sqlalchemy import Column, BigInteger, String, UniqueConstraint, Integer
from ._base import Base


class Character(Base):
    __tablename__ = "character"

    id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True)
    mal_id = Column(BigInteger)
    name = Column(String)
    name_kanji = Column(String)
    character_image = Column(String)
    about = Column(String)
    lol = Column(String)

    __table_args__ = (UniqueConstraint("mal_id", "name", "name_kanji", name="_name_uc"),)
