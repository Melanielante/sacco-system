from sqlalchemy.orm import relationship
from .models import Member, Account, SavingsTransaction, Loan, LoanRepayment

# Relationships 

# Member - Account (One-to-Many)
Member.accounts = relationship(
    "Account",
    back_populates="member",
    cascade="all, delete-orphan"
)
Account.member = relationship("Member", back_populates="accounts")


def member_repr(self):
    return f"<Member(id={self.id}, name={self.firstname} {self.lastname}, email={self.email})>"
Member.__repr__ = member_repr

def account_repr(self):
    return f"<Account(id={self.id}, number={self.account_number}, balance={self.balance}, type={self.account_type})>"
Account.__repr__ = account_repr


# Account - SavingsTransaction (One-to-Many)
Account.savings_transactions = relationship(
    "SavingsTransaction",
    back_populates="account",
    cascade="all, delete-orphan"
)
SavingsTransaction.account = relationship("Account", back_populates="savings_transactions")


def savings_repr(self):
    return f"<SavingsTransaction(id={self.id}, amount={self.amount}, type={self.transaction_type}, date={self.transaction_date})>"
SavingsTransaction.__repr__ = savings_repr


# Member - Loan (One-to-Many)
Member.loans = relationship(
    "Loan",
    back_populates="member",
    cascade="all, delete-orphan"
)
Loan.member = relationship("Member", back_populates="loans")


def loan_repr(self):
    return f"<Loan(id={self.id}, principal={self.principle_amount}, interest={self.interest_rate}, status={self.status})>"
Loan.__repr__ = loan_repr


# Loan - LoanRepayment (One-to-Many)
Loan.loan_repayments = relationship(
    "LoanRepayment",
    back_populates="loan",
    cascade="all, delete-orphan"
)
LoanRepayment.loan = relationship("Loan", back_populates="loan_repayments")


def repayment_repr(self):
    return f"<LoanRepayment(id={self.id}, amount={self.amount}, method={self.method}, repayable_date={self.repayable_date})>"
LoanRepayment.__repr__ = repayment_repr
