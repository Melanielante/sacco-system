from .models import Member, Account, SavingsTransaction, Loan, LoanRepayment 
from .db import session, SessionLocal
from datetime import datetime


session = SessionLocal()
#  Member 
def add_member(firstname, lastname, age, email, phone):
    new_member = Member(
        firstname=firstname,
        lastname=lastname,
        age=age,
        email=email,
        phone=phone,
        join_date=datetime.now()
    )
    session.add(new_member)
    session.commit()
    return new_member

def get_member_by_id(member_id):
    return session.query(Member).filter_by(id=member_id).first()

def get_all_members():
    return session.query(Member).all()

def update_member(member_id, **kwargs):
    member = get_member_by_id(member_id)
    if member:
        for key, value in kwargs.items():
            if hasattr(member, key):
                setattr(member, key, value)
        session.commit()
    return member

def delete_member(member_id):
    member = get_member_by_id(member_id)
    if member:
        session.delete(member)
        session.commit()

#  Account 
def add_account(member_id, account_number, balance=0.0, account_type="savings"):
    new_account = Account(
        member_id=member_id,
        account_number=account_number,
        balance=balance,
        account_type=account_type
    )
    session.add(new_account)
    session.commit()
    return new_account

def get_account_by_id(account_id):
    return session.query(Account).filter_by(id=account_id).first()

def get_all_accounts():
    return session.query(Account).all()

def update_account(account_id, **kwargs):
    account = get_account_by_id(account_id)
    if account:
        for key, value in kwargs.items():
            if hasattr(account, key):
                setattr(account, key, value)
        session.commit()
    return account

def delete_account(account_id):
    account = get_account_by_id(account_id)
    if account:
        session.delete(account)
        session.commit()

#  SavingsTransaction 
def add_savings_transaction(account_id, amount, transaction_type):
    new_transaction = SavingsTransaction(
        account_id=account_id,
        amount=amount,
        transaction_type=transaction_type,
        transaction_date=datetime.now()
    )
    session.add(new_transaction)
    session.commit()
    return new_transaction

def get_transaction_by_id(transaction_id):
    return session.query(SavingsTransaction).filter_by(id=transaction_id).first()

def get_all_transactions():
    return session.query(SavingsTransaction).all()

def update_transaction(transaction_id, **kwargs):
    transaction = get_transaction_by_id(transaction_id)
    if transaction:
        for key, value in kwargs.items():
            if hasattr(transaction, key):
                setattr(transaction, key, value)
        session.commit()
    return transaction

def delete_transaction(transaction_id):
    transaction = get_transaction_by_id(transaction_id)
    if transaction:
        session.delete(transaction)
        session.commit()

#  Loan 
def add_loan(member_id, principle_amount, interest_rate, status="pending"):
    new_loan = Loan(
        member_id=member_id,
        principle_amount=principle_amount,
        interest_rate=interest_rate,
        status=status,
        issue_ddate=datetime.now()
    )
    session.add(new_loan)
    session.commit()
    return new_loan

def get_loan_by_id(loan_id):
    return session.query(Loan).filter_by(id=loan_id).first()

def get_all_loans():
    return session.query(Loan).all()

def update_loan(loan_id, **kwargs):
    loan = get_loan_by_id(loan_id)
    if loan:
        for key, value in kwargs.items():
            if hasattr(loan, key):
                setattr(loan, key, value)
        session.commit()
    return loan

def delete_loan(loan_id):
    loan = get_loan_by_id(loan_id)
    if loan:
        session.delete(loan)
        session.commit()

#  LoanRepayment 
def add_loan_repayment(loan_id, amount, repayable_date, method):
    new_repayment = LoanRepayment(
        loan_id=loan_id,
        amount=amount,
        repayable_date=repayable_date,
        method=method
    )
    session.add(new_repayment)
    session.commit()
    return new_repayment

def get_repayment_by_id(repayment_id):
    return session.query(LoanRepayment).filter_by(id=repayment_id).first()

def get_all_repayments():
    return session.query(LoanRepayment).all()

def update_repayment(repayment_id, **kwargs):
    repayment = get_repayment_by_id(repayment_id)
    if repayment:
        for key, value in kwargs.items():
            if hasattr(repayment, key):
                setattr(repayment, key, value)
        session.commit()
    return repayment

def delete_repayment(repayment_id):
    repayment = get_repayment_by_id(repayment_id)
    if repayment:
        session.delete(repayment)
        session.commit()
