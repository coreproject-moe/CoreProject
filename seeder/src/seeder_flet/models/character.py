# models.py
from sqlalchemy import Column, BigInteger, String, UniqueConstraint
from ._base import Base


class Character(Base):
    __tablename__ = "character"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    mal_id = Column(BigInteger, index=True)
    name = Column(String, index=True)
    name_kanji = Column(String)
    character_image = Column(String)
    about = Column(String)

    __table_args__ = (UniqueConstraint("mal_id", "name", "name_kanji", name="_name_uc"),)
