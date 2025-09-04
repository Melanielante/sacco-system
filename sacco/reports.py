from .crud import get_all_members, get_all_accounts, get_all_loans, get_all_transactions, get_all_repayments


# LISTS 
def list_all_member_names():
    """Return a list of all member full names."""
    members = get_all_members()
    return [f"{m.firstname} {m.lastname}" for m in members]


def list_all_account_balances():
    """Return a list of all account balances."""
    accounts = get_all_accounts()
    return [acc.balance for acc in accounts]


# TUPLES 
def loan_summary():
    """Return a list of tuples with loan details (id, member_id, amount, status)."""
    loans = get_all_loans()
    return [(loan.id, loan.member_id, loan.principle_amount, loan.status) for loan in loans]


def repayment_summary():
    """Return a list of tuples with repayment details (id, loan_id, amount, method)."""
    repayments = get_all_repayments()
    return [(r.id, r.loan_id, r.amount, r.method) for r in repayments]


# DICTIONARIES 
def member_account_map():
    """Return a dictionary mapping member_id -> list of account numbers."""
    accounts = get_all_accounts()
    mapping = {}
    for acc in accounts:
        mapping.setdefault(acc.member_id, []).append(acc.account_number)
    return mapping


def transaction_map():
    """Return a dictionary mapping account_id -> list of transactions (as tuples)."""
    transactions = get_all_transactions()
    mapping = {}
    for t in transactions:
        entry = (t.id, t.amount, t.transaction_type, t.transaction_date)
        mapping.setdefault(t.account_id, []).append(entry)
    return mapping


# COMBINED REPORTS 
def loan_report_by_member():
    """Return a dictionary mapping member_id -> list of loan tuples (id, amount, status)."""
    loans = get_all_loans()
    report = {}
    for loan in loans:
        entry = (loan.id, loan.principle_amount, loan.status)
        report.setdefault(loan.member_id, []).append(entry)
    return report


def savings_overview():
    """Return a dictionary with summary statistics about savings transactions."""
    transactions = get_all_transactions()
    deposits = sum(t.amount for t in transactions if t.transaction_type == "deposit")
    withdrawals = sum(t.amount for t in transactions if t.transaction_type == "withdrawal")
    return {
        "total_transactions": len(transactions),
        "total_deposits": deposits,
        "total_withdrawals": withdrawals,
        "net_savings": deposits - withdrawals
    }
