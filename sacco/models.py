from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from .db import Base, engine


class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    age = Column(Integer)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    join_date = Column(DateTime)


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    account_number = Column(String(40), nullable=False, unique=True)
    balance = Column(Float(10, 4), default=0.0)
    account_type = Column(String(30), nullable=False)

    member_id = Column(Integer, ForeignKey('members.id'), nullable=False)


class SavingsTransaction(Base):
    __tablename__ = "savings_transactions"

    id = Column(Integer, primary_key=True)
    amount = Column(Float(10, 4), nullable=False)
    transaction_date = Column(DateTime)
    transaction_type = Column(String(50), nullable=False)

    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True)
    principle_amount = Column(Float(10, 4), nullable=False)
    interest_rate = Column(Float(5, 2), nullable=False)  
    status = Column(String(20), default="pending")
    issue_date = Column(DateTime)

    member_id = Column(Integer, ForeignKey('members.id'), nullable=False)


class LoanRepayment(Base):
    __tablename__ = "loan_repayments"

    id = Column(Integer, primary_key=True)
    amount = Column(Float(10, 4), nullable=False)
    repayable_date = Column(DateTime)
    method = Column(String(40), nullable=False)

    loan_id = Column(Integer, ForeignKey('loans.id'), nullable=False)



if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
