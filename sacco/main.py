import click
import re
from datetime import datetime

from .crud import (
    add_member, get_member_by_id, get_all_members, update_member, delete_member,
    add_account, get_account_by_id, get_all_accounts, update_account, delete_account,
    add_savings_transaction, get_transaction_by_id, get_all_transactions, update_transaction, delete_transaction,
    add_loan, get_loan_by_id, get_all_loans, update_loan, delete_loan,
    add_loan_repayment, get_repayment_by_id, get_all_repayments, update_repayment, delete_repayment
)

# Import reports (printing functions)
from .reports import (
    list_all_member_names,
    list_all_account_balances,
    loan_summary,
    repayment_summary,
    member_account_map,
    transaction_map,
    loan_report_by_member,
    savings_overview
)


#  HELPERS 
def safe_prompt(text, ptype=str, default=None, validator=None):
    """Prompt safely with type checking & optional custom validation."""
    while True:
        try:
            value = click.prompt(text, type=ptype, default=default)
            if validator and not validator(value):
                raise ValueError("Validation failed")
            return value
        except (ValueError, TypeError):
            click.secho(" Invalid input. Please try again.", fg="red")


def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def validate_phone(phone):
    return phone.isdigit() and (7 <= len(phone) <= 15)


# MAIN MENU 
while True:
    click.secho("\n====== SACCO SYSTEM ======", fg="blue", bold=True)
    click.secho("1. Members", fg="yellow")
    click.secho("2. Accounts", fg="yellow")
    click.secho("3. Savings Transactions", fg="yellow")
    click.secho("4. Loans", fg="yellow")
    click.secho("5. Loan Repayments", fg="yellow")
    click.secho("6. Reports", fg="green")
    click.secho("7. Exit", fg="red")

    choice = safe_prompt("Select an option", int)

    #  MEMBERS 
    if choice == 1:
        click.secho("\n--- Members Menu ---", fg="blue")
        click.secho("1. Add Member", fg="yellow")
        click.secho("2. View All Members", fg="yellow")
        click.secho("3. View Member by ID", fg="yellow")
        click.secho("4. Update Member", fg="yellow")
        click.secho("5. Delete Member", fg="yellow")

        member_choice = safe_prompt("Select an option", int)

        if member_choice == 1:
            firstname = safe_prompt("First Name")
            lastname = safe_prompt("Last Name")
            age = safe_prompt("Age", int)
            email = safe_prompt("Email", validator=validate_email)
            phone = safe_prompt("Phone", validator=validate_phone)
            add_member(firstname, lastname, age, email, phone)
            click.secho(f" Member {firstname} {lastname} added successfully!", fg="green")

        elif member_choice == 2:
            members = get_all_members()
            for m in members:
                click.secho(f"{m.id}: {m.firstname} {m.lastname}, {m.email}, {m.phone}", fg="cyan")

        elif member_choice == 3:
            mid = safe_prompt("Enter Member ID", int)
            m = get_member_by_id(mid)
            if m:
                click.secho(f"{m.id}: {m.firstname} {m.lastname}, {m.email}, {m.phone}", fg="cyan")
            else:
                click.secho(" Member not found!", fg="red")

        elif member_choice == 4:
            mid = safe_prompt("Enter Member ID", int)
            field = safe_prompt("Field to update (firstname, lastname, age, email, phone)")
            if field not in ["firstname", "lastname", "age", "email", "phone"]:
                click.secho(" Invalid field!", fg="red")
            else:
                value = safe_prompt("New Value")
                update_member(mid, **{field: value})
                click.secho("Member updated successfully!", fg="green")

        elif member_choice == 5:
            mid = safe_prompt("Enter Member ID", int)
            delete_member(mid)
            click.secho(" Member deleted successfully!", fg="red")

    # ACCOUNTS 
    elif choice == 2:
        click.secho("\n--- Accounts Menu ---", fg="blue")
        click.secho("1. Add Account", fg="yellow")
        click.secho("2. View All Accounts", fg="yellow")
        click.secho("3. View Account by ID", fg="yellow")
        click.secho("4. Update Account", fg="yellow")
        click.secho("5. Delete Account", fg="yellow")

        account_choice = safe_prompt("Select an option", int)

        if account_choice == 1:
            member_id = safe_prompt("Member ID", int)
            acc_no = safe_prompt("Account Number")
            balance = safe_prompt("Initial Balance", float)
            acc_type = safe_prompt("Account Type (savings/loan)", default="savings")
            if acc_type not in ["savings", "loan"]:
                click.secho(" Invalid account type!", fg="red")
            else:
                add_account(member_id, acc_no, balance, acc_type)
                click.secho(" Account added successfully!", fg="green")

        elif account_choice == 2:
            accounts = get_all_accounts()
            for a in accounts:
                click.secho(f"{a.id}: {a.account_number}, Balance={a.balance}, Type={a.account_type}", fg="cyan")

        elif account_choice == 3:
            aid = safe_prompt("Enter Account ID", int)
            a = get_account_by_id(aid)
            if a:
                click.secho(f"{a.id}: {a.account_number}, Balance={a.balance}, Type={a.account_type}", fg="cyan")
            else:
                click.secho(" Account not found!", fg="red")

        elif account_choice == 4:
            aid = safe_prompt("Enter Account ID", int)
            field = safe_prompt("Field to update (balance, account_type)")
            if field not in ["balance", "account_type"]:
                click.secho(" Invalid field!", fg="red")
            else:
                value = safe_prompt("New Value")
                update_account(aid, **{field: value})
                click.secho(" Account updated successfully!", fg="green")

        elif account_choice == 5:
            aid = safe_prompt("Enter Account ID", int)
            delete_account(aid)
            click.secho(" Account deleted successfully!", fg="red")

    # REPORTS 
    elif choice == 6:
        click.secho("\n--- Reports Menu ---", fg="blue")
        click.secho("1. List All Member Names", fg="yellow")
        click.secho("2. List All Account Balances", fg="yellow")
        click.secho("3. Loan Summary", fg="yellow")
        click.secho("4. Repayment Summary", fg="yellow")
        click.secho("5. Member → Account Map", fg="yellow")
        click.secho("6. Account → Transactions Map", fg="yellow")
        click.secho("7. Loan Report by Member", fg="yellow")
        click.secho("8. Savings Overview", fg="yellow")

        report_choice = safe_prompt("Select a report", int)

        if report_choice == 1:
            for name in list_all_member_names():
                click.secho(name, fg="cyan")

        elif report_choice == 2:
            for bal in list_all_account_balances():
                click.secho(f"Balance: {bal}", fg="cyan")

        elif report_choice == 3:
            for l in loan_summary():
                click.secho(f"Loan {l[0]}: Member {l[1]}, Amount={l[2]}, Status={l[3]}", fg="cyan")

        elif report_choice == 4:
            for r in repayment_summary():
                click.secho(f"Repayment {r[0]}: Loan {r[1]}, Amount={r[2]}, Method={r[3]}", fg="cyan")

        elif report_choice == 5:
            mapping = member_account_map()
            for mid, accs in mapping.items():
                click.secho(f"Member {mid}: Accounts {accs}", fg="cyan")

        elif report_choice == 6:
            mapping = transaction_map()
            for aid, txns in mapping.items():
                click.secho(f"Account {aid}: {txns}", fg="cyan")

        elif report_choice == 7:
            report = loan_report_by_member()
            for mid, loans in report.items():
                click.secho(f"Member {mid}: {loans}", fg="cyan")

        elif report_choice == 8:
            stats = savings_overview()
            for k, v in stats.items():
                click.secho(f"{k}: {v}", fg="cyan")

    elif choice == 7:
        click.secho(" Goodbye!", fg="green")
        break
