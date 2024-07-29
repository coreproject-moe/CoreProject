from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine(os.environ.get("DATABASE_URL"))
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
