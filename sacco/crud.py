from .models import Member, Account, SavingsTransaction, Loan, LoanRepayment
from .db import SessionLocal
from datetime import datetime
import re
from sqlalchemy.exc import SQLAlchemyError


# UTILITIES 
def get_session():
    """Context-managed session factory."""
    return SessionLocal()


def is_valid_email(email: str) -> bool:
    """Simple email format validation."""
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email) is not None


# MEMBER CRUD 
def add_member(firstname, lastname, age, email, phone):
    if age < 18:
        raise ValueError("Member must be at least 18 years old.")
    if not is_valid_email(email):
        raise ValueError("Invalid email format.")

    with get_session() as session:
        try:
            if session.query(Member).filter_by(email=email).first():
                raise ValueError("Email already exists.")

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
            session.refresh(new_member)
            return new_member
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Database error while adding member: {e}")


def get_member_by_id(member_id):
    with get_session() as session:
        return session.query(Member).filter_by(id=member_id).first()


def get_all_members():
    with get_session() as session:
        return session.query(Member).all()


def update_member(member_id, **kwargs):
    with get_session() as session:
        member = session.query(Member).filter_by(id=member_id).first()
        if not member:
            raise ValueError("Member not found.")

        for key, value in kwargs.items():
            if hasattr(member, key):
                if key == "email" and not is_valid_email(value):
                    raise ValueError("Invalid email format.")
                setattr(member, key, value)

        try:
            session.commit()
            session.refresh(member)
            return member
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Database error while updating member: {e}")


def delete_member(member_id):
    with get_session() as session:
        member = session.query(Member).filter_by(id=member_id).first()
        if not member:
            raise ValueError("Member not found.")

        try:
            session.delete(member)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Database error while deleting member: {e}")


# ACCOUNT CRUD 
def add_account(member_id, account_number, balance=0.0, account_type="savings"):
    if balance < 0:
        raise ValueError("Initial balance cannot be negative.")

    with get_session() as session:
        if not session.query(Member).filter_by(id=member_id).first():
            raise ValueError("Member does not exist.")
        if session.query(Account).filter_by(account_number=account_number).first():
            raise ValueError("Account number already exists.")

        try:
            new_account = Account(
                member_id=member_id,
                account_number=account_number,
                balance=balance,
                account_type=account_type
            )
            session.add(new_account)
            session.commit()
            session.refresh(new_account)
            return new_account
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Database error while adding account: {e}")


def get_account_by_id(account_id):
    with get_session() as session:
        return session.query(Account).filter_by(id=account_id).first()


def get_all_accounts():
    with get_session() as session:
        return session.query(Account).all()


def update_account(account_id, **kwargs):
    with get_session() as session:
        account = session.query(Account).filter_by(id=account_id).first()
        if not account:
            raise ValueError("Account not found.")

        for key, value in kwargs.items():
            if hasattr(account, key):
                setattr(account, key, value)

        try:
            session.commit()
            session.refresh(account)
            return account
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Database error while updating account: {e}")


def delete_account(account_id):
    with get_session() as session:
        account = session.query(Account).filter_by(id=account_id).first()
        if not account:
            raise ValueError("Account not found.")

        try:
            session.delete(account)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Database error while deleting account: {e}")


# SAVINGS TRANSACTION CRUD 
def add_savings_transaction(account_id, amount, transaction_type):
    if amount <= 0:
        raise ValueError("Transaction amount must be positive.")
    if transaction_type not in ["deposit", "withdrawal"]:
        raise ValueError("Invalid transaction type.")

    with get_session() as session:
        account = session.query(Account).filter_by(id=account_id).first()
        if not account:
            raise ValueError("Account does not exist.")

        if transaction_type == "withdrawal" and account.balance < amount:
            raise ValueError("Insufficient balance for withdrawal.")

        try:
            new_transaction = SavingsTransaction(
                account_id=account_id,
                amount=amount,
                transaction_type=transaction_type,
                transaction_date=datetime.now()
            )
            if transaction_type == "deposit":
                account.balance += amount
            else:
                account.balance -= amount

            session.add(new_transaction)
            session.commit()
            session.refresh(new_transaction)
            return new_transaction
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Database error while adding transaction: {e}")


def get_transaction_by_id(transaction_id):
    with get_session() as session:
        return session.query(SavingsTransaction).filter_by(id=transaction_id).first()


def get_all_transactions():
    with get_session() as session:
        return session.query(SavingsTransaction).all()


def update_transaction(transaction_id, **kwargs):
    with get_session() as session:
        transaction = session.query(SavingsTransaction).filter_by(id=transaction_id).first()
        if not transaction:
            raise ValueError("Transaction not found.")

        for key, value in kwargs.items():
            if hasattr(transaction, key):
                setattr(transaction, key, value)

        try:
            session.commit()
            session.refresh(transaction)
            return transaction
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Database error while updating transaction: {e}")


def delete_transaction(transaction_id):
    with get_session() as session:
        transaction = session.query(SavingsTransaction).filter_by(id=transaction_id).first()
        if not transaction:
            raise ValueError("Transaction not found.")

        try:
            session.delete(transaction)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Database error while deleting transaction: {e}")


# ---------------------- LOAN CRUD ---------------------- #
def add_loan(member_id, principle_amount, interest_rate, status="pending"):
    if principle_amount <= 0:
        raise ValueError("Loan amount must be positive.")
    if interest_rate <= 0:
        raise ValueError("Interest rate must be positive.")

    with get_session() as session:
        if not session.query(Member).filter_by(id=member_id).first():
            raise ValueError("Member does not exist.")

        try:
            new_loan = Loan(
                member_id=member_id,
                principle_amount=principle_amount,
                interest_rate=interest_rate,
                status=status,
                issue_date=datetime.now()
            )
            session.add(new_loan)
            session.commit()
            session.refresh(new_loan)
            return new_loan
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Database error while adding loan: {e}")


def get_loan_by_id(loan_id):
    with get_session() as session:
        return session.query(Loan).filter_by(id=loan_id).first()


def get_all_loans():
    with get_session() as session:
        return session.query(Loan).all()


def update_loan(loan_id, **kwargs):
    with get_session() as session:
        loan = session.query(Loan).filter_by(id=loan_id).first()
        if not loan:
            raise ValueError("Loan not found.")

        for key, value in kwargs.items():
            if hasattr(loan, key):
                setattr(loan, key, value)

        try:
            session.commit()
            session.refresh(loan)
            return loan
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Database error while updating loan: {e}")


def delete_loan(loan_id):
    with get_session() as session:
        loan = session.query(Loan).filter_by(id=loan_id).first()
        if not loan:
            raise ValueError("Loan not found.")

        try:
            session.delete(loan)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Database error while deleting loan: {e}")


# LOAN REPAYMENT CRUD 
def add_loan_repayment(loan_id, amount, repayable_date, method):
    if amount <= 0:
        raise ValueError("Repayment amount must be positive.")

    with get_session() as session:
        loan = session.query(Loan).filter_by(id=loan_id).first()
        if not loan:
            raise ValueError("Loan does not exist.")

        try:
            new_repayment = LoanRepayment(
                loan_id=loan_id,
                amount=amount,
                repayable_date=repayable_date,
                method=method
            )
            session.add(new_repayment)

            # reduce loan balance
            loan.principle_amount -= amount
            if loan.principle_amount <= 0:
                loan.status = "paid"

            session.commit()
            session.refresh(new_repayment)
            return new_repayment
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Database error while adding loan repayment: {e}")


def get_repayment_by_id(repayment_id):
    with get_session() as session:
        return session.query(LoanRepayment).filter_by(id=repayment_id).first()


def get_all_repayments():
    with get_session() as session:
        return session.query(LoanRepayment).all()


def update_repayment(repayment_id, **kwargs):
    with get_session() as session:
        repayment = session.query(LoanRepayment).filter_by(id=repayment_id).first()
        if not repayment:
            raise ValueError("Repayment not found.")

        for key, value in kwargs.items():
            if hasattr(repayment, key):
                setattr(repayment, key, value)

        try:
            session.commit()
            session.refresh(repayment)
            return repayment
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Database error while updating repayment: {e}")


def delete_repayment(repayment_id):
    with get_session() as session:
        repayment = session.query(LoanRepayment).filter_by(id=repayment_id).first()
        if not repayment:
            raise ValueError("Repayment not found.")

        try:
            session.delete(repayment)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Database error while deleting repayment: {e}")
