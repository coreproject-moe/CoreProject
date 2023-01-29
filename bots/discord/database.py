from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from settings import POSTGRES

NAME = POSTGRES["NAME"]
USER = POSTGRES["USER"]
PASSWORD = POSTGRES["PASSWORD"]
HOST = POSTGRES.get("HOST") or "localhost"
PORT = POSTGRES.get("PORT") or "5432"

engine = create_async_engine(
    f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}", echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, class_=AsyncSession)

django_engine = create_async_engine(
    f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/django", echo=True
)
DjangoSessionLocal = sessionmaker(autocommit=False, autoflush=False, class_=AsyncSession)

BASE = declarative_base()
