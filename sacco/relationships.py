
from sqlalchemy.orm import relationship
from .models import Member, Account, SavingsTransaction, Loan, LoanRepayment

# Member - Account (One-to-Many)
Member.accounts = relationship("Account", back_populates="member", cascade="all, delete-orphan")
Account.member = relationship("Member", back_populates="accounts")

# Account - SavingsTransaction (One-to-Many)
Account.savings_transactions = relationship("SavingsTransaction", back_populates="account", cascade="all, delete-orphan")
SavingsTransaction.account = relationship("Account", back_populates="savings_transactions")

# Member - Loan (One-to-Many)
Member.loans = relationship("Loan", back_populates="member", cascade="all, delete-orphan")
Loan.member = relationship("Member", back_populates="loans")

# LoanRepayment relationships (One-to-Many)
Loan.loan_repayments = relationship("LoanRepayment", back_populates="loan", cascade="all, delete-orphan")
LoanRepayment.loan = relationship("Loan", back_populates="loan_repayments")
