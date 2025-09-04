import click
from .crud import (
    get_all_members, get_all_accounts, get_all_loans, 
    get_all_transactions, get_all_repayments
)

# LISTS 
def list_all_member_names():
    members = get_all_members()
    return [f"{m.firstname} {m.lastname}" for m in members]


def list_all_account_balances():
    accounts = get_all_accounts()
    return [acc.balance for acc in accounts]


# TUPLES
def loan_summary():
    loans = get_all_loans()
    return [(loan.id, loan.member_id, loan.principle_amount, loan.status) for loan in loans]


def repayment_summary():
    repayments = get_all_repayments()
    return [(r.id, r.loan_id, r.amount, r.method) for r in repayments]


#  DICTIONARIES 
def member_account_map():
    accounts = get_all_accounts()
    mapping = {}
    for acc in accounts:
        mapping.setdefault(acc.member_id, []).append(acc.account_number)
    return mapping


def transaction_map():
    transactions = get_all_transactions()
    mapping = {}
    for t in transactions:
        entry = (t.id, t.amount, t.transaction_type, t.transaction_date)
        mapping.setdefault(t.account_id, []).append(entry)
    return mapping


# COMBINED REPORTS 
def loan_report_by_member():
    loans = get_all_loans()
    report = {}
    for loan in loans:
        entry = (loan.id, loan.principle_amount, loan.status)
        report.setdefault(loan.member_id, []).append(entry)
    return report


def savings_overview():
    transactions = get_all_transactions()
    deposits = sum(t.amount for t in transactions if t.transaction_type == "deposit")
    withdrawals = sum(t.amount for t in transactions if t.transaction_type == "withdrawal")
    return {
        "total_transactions": len(transactions),
        "total_deposits": deposits,
        "total_withdrawals": withdrawals,
        "net_savings": deposits - withdrawals
    }


#  PRETTY PRINT HELPERS 
def print_list(title, items):
    click.secho(f"\n{title}", fg="blue", bold=True)
    for i in items:
        click.secho(f"- {i}", fg="cyan")


def print_tuples(title, tuples):
    click.secho(f"\n{title}", fg="blue", bold=True)
    for tup in tuples:
        click.secho(f"{tup}", fg="cyan")


def print_dict(title, dct):
    click.secho(f"\n{title}", fg="blue", bold=True)
    for key, value in dct.items():
        click.secho(f"{key}: {value}", fg="cyan")
