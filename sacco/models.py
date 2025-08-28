# models.py
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from .db import Base, engine

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    age = Column(Integer)
    email = Column(String, unique=True)
    phone = Column(String, unique=True)
    join_date = Column(DateTime)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    account_number = Column(String(40), nullable=False)
    balance = Column(Float(10,4))
    account_type = Column(String(30))

    member_id = Column(Integer, ForeignKey('member.id'))


class SavingsTransaction(Base):
    __tablename__ = "savingsTransactions"


    id = Column(Integer, primary_key=True)
    amount = Column(Float(10,4))
    transaction_date = Column(DateTime)
    transaction_type = Column(String(50))

    account_id = Column(Integer, ForeignKey('account.id'))


class Loan(Base):
    __tablename__ = "loans"


    id = Column(Integer, primary_key=True)
    principle_amount = Column(Float(10,4), nullable=False)
    interest_rate = Column(String(10), nullable=False)
    status = Column(String(20))
    issue_ddate = Column(DateTime)

    member_id = Column(Integer, ForeignKey('member.id'))


class LoanRepayment(Base):
    __tablename__ = "loanRepayments"


    id = Column(Integer, primary_key=True)
    amount = Column(Float(10,4))
    repayable_date = Column(DateTime)
    method = Column(String(40))


    loan_id = Column(Integer, ForeignKey('loan.id'))