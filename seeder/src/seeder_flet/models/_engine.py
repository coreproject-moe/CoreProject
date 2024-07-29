from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
import os


engine = create_async_engine(os.environ.get("DATABASE_URL"), echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
