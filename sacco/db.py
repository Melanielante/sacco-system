# sacco/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///saccoSystem.db"

engine = create_engine(
    DATABASE_URL, 
    echo=True
)
SessionLocal = sessionmaker(bind=engine)


Base = declarative_base()
