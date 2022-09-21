from .settings import POSTGRES
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker


NAME = POSTGRES["NAME"]
USER = POSTGRES["USER"]
PASSWORD = POSTGRES["PASSWORD"]
HOST = POSTGRES.get("HOST") or "localhost"
PORT = POSTGRES.get("PORT") or "5432"

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, class_=AsyncSession)


BASE = declarative_base()
