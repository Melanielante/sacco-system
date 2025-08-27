from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# database URL
DATABASE_URL = "sqlite:///saccoSystem.db"

engine = create_engine (
    DATABASE_URL
)

SessionLocal = sessionmaker(
    autocommit = False,
    bind = engine,
    autoflush = False
)

Base = declarative_base()
