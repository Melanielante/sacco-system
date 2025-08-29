
from models import Member, Account, SavingsTransaction, Loan, LoanRepayment, session

#  Member 
#creating new member
def add_member(name, email, phone):
    new_member = Member(name=name, email=email, phone=phone)
    session.add(new_member)
    session.commit()
    return new_member

def get_member_by_id(member_id):
    return session.query(Member).filter_by(id=member_id).first()

def get_all_members():
    return session.query(Member).all()

#updating member
def update_member(member_id, **kwargs):
    member = get_member_by_id(member_id)
    if member:
        for key, value in kwargs.items():
            setattr(member, key, value)
        session.commit()
    return member

#deleting member
def delete_member(member_id):
    member = get_member_by_id(member_id)
    if member:
        session.delete(member)
        session.commit()

#  Account 
#creating new account
def add_account(member_id, account_number, balance=0.0):
    new_account = Account(member_id=member_id, account_number=account_number, balance=balance)
    session.add(new_account)
    session.commit()
    return new_account

def get_account_by_id(account_id):
    return session.query(Account).filter_by(id=account_id).first()

def get_all_accounts():
    return session.query(Account).all()

#updating accounts
def update_account(account_id, **kwargs):
    account = get_account_by_id(account_id)
    if account:
        for key, value in kwargs.items():
            setattr(account, key, value)
        session.commit()
    return account

#deleting accountts
def delete_account(account_id):
    account = get_account_by_id(account_id)
    if account:
        session.delete(account)
        session.commit()

#  SavingsTransaction 
#add savings transactions
def add_savings_transaction(account_id, amount, transaction_type):
    new_transaction = SavingsTransaction(account_id=account_id, amount=amount, transaction_type=transaction_type)
    session.add(new_transaction)
    session.commit()
    return new_transaction

#reading
def get_transaction_by_id(transaction_id):
    return session.query(SavingsTransaction).filter_by(id=transaction_id).first()

def get_all_transactions():
    return session.query(SavingsTransaction).all()

#update
def update_transaction(transaction_id, **kwargs):
    transaction = get_transaction_by_id(transaction_id)
    if transaction:
        for key, value in kwargs.items():
            setattr(transaction, key, value)
        session.commit()
    return transaction

#delete
def delete_transaction(transaction_id):
    transaction = get_transaction_by_id(transaction_id)
    if transaction:
        session.delete(transaction)
        session.commit()

#  Loan 
#adding
def add_loan(member_id, amount, interest_rate, status="pending"):
    new_loan = Loan(member_id=member_id, amount=amount, interest_rate=interest_rate, status=status)
    session.add(new_loan)
    session.commit()
    return new_loan

#reading loans
def get_loan_by_id(loan_id):
    return session.query(Loan).filter_by(id=loan_id).first()

def get_all_loans():
    return session.query(Loan).all()

# updating loans
def update_loan(loan_id, **kwargs):
    loan = get_loan_by_id(loan_id)
    if loan:
        for key, value in kwargs.items():
            setattr(loan, key, value)
        session.commit()
    return loan

#deleting loans
def delete_loan(loan_id):
    loan = get_loan_by_id(loan_id)
    if loan:
        session.delete(loan)
        session.commit()

#  LoanRepayment 
#adding 
def add_loan_repayment(loan_id, amount, repayment_date):
    new_repayment = LoanRepayment(loan_id=loan_id, amount=amount, repayment_date=repayment_date)
    session.add(new_repayment)
    session.commit()
    return new_repayment

def get_repayment_by_id(repayment_id):
    return session.query(LoanRepayment).filter_by(id=repayment_id).first()

def get_all_repayments():
    return session.query(LoanRepayment).all()

# updating
def update_repayment(repayment_id, **kwargs):
    repayment = get_repayment_by_id(repayment_id)
    if repayment:
        for key, value in kwargs.items():
            setattr(repayment, key, value)
        session.commit()
    return repayment

#deleting 
def delete_repayment(repayment_id):
    repayment = get_repayment_by_id(repayment_id)
    if repayment:
        session.delete(repayment)
        session.commit()
