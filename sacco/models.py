# models.py
from sqlalchemy import Column, Integer, String, DateTime
from .db import Base, engine

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, unique=True)
    phone = Column(String, unique=True)
    join_date = Column(DateTime)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

