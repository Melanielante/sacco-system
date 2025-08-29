import click
from .crud import (
    add_member, get_member_by_id, get_all_members, update_member, delete_member,
    add_account, get_account_by_id, get_all_accounts, update_account, delete_account,
    add_savings_transaction, get_transaction_by_id, get_all_transactions, update_transaction, delete_transaction,
    add_loan, get_loan_by_id, get_all_loans, update_loan, delete_loan,
    add_loan_repayment, get_repayment_by_id, get_all_repayments, update_repayment, delete_repayment
)
from datetime import datetime

while True:
    click.secho("\n====== SACCO SYSTEM ======", fg="blue", bold=True)
    click.secho("1. Members", fg="yellow")
    click.secho("2. Accounts", fg="yellow")
    click.secho("3. Savings Transactions", fg="yellow")
    click.secho("4. Loans", fg="yellow")
    click.secho("5. Loan Repayments", fg="yellow")
    click.secho("6. Exit", fg="red")

    choice = click.prompt("Select an option", type=int)

    # ------------------ MEMBERS ------------------
    if choice == 1:
        click.secho("\n--- Members Menu ---", fg="blue")
        click.secho("1. Add Member", fg="yellow")
        click.secho("2. View All Members", fg="yellow")
        click.secho("3. View Member by ID", fg="yellow")
        click.secho("4. Update Member", fg="yellow")
        click.secho("5. Delete Member", fg="yellow")

        member_choice = click.prompt("Select an option", type=int)

        if member_choice == 1:
            firstname = click.prompt("First Name")
            lastname = click.prompt("Last Name")
            age = click.prompt("Age", type=int)
            email = click.prompt("Email")
            phone = click.prompt("Phone")
            add_member(firstname, lastname, age, email, phone)
            click.secho(f"Member {firstname} {lastname} added successfully!", fg="green")

        elif member_choice == 2:
            members = get_all_members()
            for m in members:
                click.secho(f"{m.id}: {m.firstname} {m.lastname}, {m.email}, {m.phone}", fg="cyan")

        elif member_choice == 3:
            mid = click.prompt("Enter Member ID", type=int)
            m = get_member_by_id(mid)
            if m:
                click.secho(f"{m.id}: {m.firstname} {m.lastname}, {m.email}, {m.phone}", fg="cyan")
            else:
                click.secho("Member not found!", fg="red")

        elif member_choice == 4:
            mid = click.prompt("Enter Member ID", type=int)
            field = click.prompt("Field to update (firstname, lastname, age, email, phone)")
            value = click.prompt("New Value")
            update_member(mid, **{field: value})
            click.secho("Member updated successfully!", fg="green")

        elif member_choice == 5:
            mid = click.prompt("Enter Member ID", type=int)
            delete_member(mid)
            click.secho("Member deleted successfully!", fg="red")

    # ------------------ ACCOUNTS ------------------
    elif choice == 2:
        click.secho("\n--- Accounts Menu ---", fg="blue")
        click.secho("1. Add Account", fg="yellow")
        click.secho("2. View All Accounts", fg="yellow")
        click.secho("3. View Account by ID", fg="yellow")
        click.secho("4. Update Account", fg="yellow")
        click.secho("5. Delete Account", fg="yellow")

        account_choice = click.prompt("Select an option", type=int)

        if account_choice == 1:
            member_id = click.prompt("Member ID", type=int)
            acc_no = click.prompt("Account Number")
            balance = click.prompt("Initial Balance", type=float)
            acc_type = click.prompt("Account Type (savings/loan)", default="savings")
            add_account(member_id, acc_no, balance, acc_type)
            click.secho("Account added successfully!", fg="green")

        elif account_choice == 2:
            accounts = get_all_accounts()
            for a in accounts:
                click.secho(f"{a.id}: {a.account_number}, Balance={a.balance}, Type={a.account_type}", fg="cyan")

        elif account_choice == 3:
            aid = click.prompt("Enter Account ID", type=int)
            a = get_account_by_id(aid)
            if a:
                click.secho(f"{a.id}: {a.account_number}, Balance={a.balance}, Type={a.account_type}", fg="cyan")
            else:
                click.secho("Account not found!", fg="red")

        elif account_choice == 4:
            aid = click.prompt("Enter Account ID", type=int)
            field = click.prompt("Field to update (balance, account_type)")
            value = click.prompt("New Value")
            update_account(aid, **{field: value})
            click.secho("Account updated successfully!", fg="green")

        elif account_choice == 5:
            aid = click.prompt("Enter Account ID", type=int)
            delete_account(aid)
            click.secho("Account deleted successfully!", fg="red")

    # ------------------ TRANSACTIONS ------------------
    elif choice == 3:
        click.secho("\n--- Savings Transactions Menu ---", fg="blue")
        click.secho("1. Add Transaction", fg="yellow")
        click.secho("2. View All Transactions", fg="yellow")
        click.secho("3. View Transaction by ID", fg="yellow")
        click.secho("4. Update Transaction", fg="yellow")
        click.secho("5. Delete Transaction", fg="yellow")

        trx_choice = click.prompt("Select an option", type=int)

        if trx_choice == 1:
            acc_id = click.prompt("Account ID", type=int)
            amt = click.prompt("Amount", type=float)
            t_type = click.prompt("Transaction Type (deposit/withdrawal)")
            add_savings_transaction(acc_id, amt, t_type)
            click.secho("Transaction added successfully!", fg="green")

        elif trx_choice == 2:
            txns = get_all_transactions()
            for t in txns:
                click.secho(f"{t.id}: Account={t.account_id}, {t.transaction_type} {t.amount} on {t.transaction_date}", fg="cyan")

        elif trx_choice == 3:
            tid = click.prompt("Enter Transaction ID", type=int)
            t = get_transaction_by_id(tid)
            if t:
                click.secho(f"{t.id}: Account={t.account_id}, {t.transaction_type} {t.amount} on {t.transaction_date}", fg="cyan")
            else:
                click.secho("Transaction not found!", fg="red")

        elif trx_choice == 4:
            tid = click.prompt("Enter Transaction ID", type=int)
            field = click.prompt("Field to update (amount, transaction_type)")
            value = click.prompt("New Value")
            update_transaction(tid, **{field: value})
            click.secho("Transaction updated successfully!", fg="green")

        elif trx_choice == 5:
            tid = click.prompt("Enter Transaction ID", type=int)
            delete_transaction(tid)
            click.secho("Transaction deleted successfully!", fg="red")

    # ------------------ LOANS ------------------
    elif choice == 4:
        click.secho("\n--- Loans Menu ---", fg="blue")
        click.secho("1. Add Loan", fg="yellow")
        click.secho("2. View All Loans", fg="yellow")
        click.secho("3. View Loan by ID", fg="yellow")
        click.secho("4. Update Loan", fg="yellow")
        click.secho("5. Delete Loan", fg="yellow")

        loan_choice = click.prompt("Select an option", type=int)

        if loan_choice == 1:
            mid = click.prompt("Member ID", type=int)
            amount = click.prompt("Principal Amount", type=float)
            rate = click.prompt("Interest Rate", type=float)
            add_loan(mid, amount, rate)
            click.secho("Loan added successfully!", fg="green")

        elif loan_choice == 2:
            loans = get_all_loans()
            for l in loans:
                click.secho(f"{l.id}: Member={l.member_id}, Amount={l.principle_amount}, Status={l.status}", fg="cyan")

        elif loan_choice == 3:
            lid = click.prompt("Enter Loan ID", type=int)
            l = get_loan_by_id(lid)
            if l:
                click.secho(f"{l.id}: Member={l.member_id}, Amount={l.principle_amount}, Status={l.status}", fg="cyan")
            else:
                click.secho("Loan not found!", fg="red")

        elif loan_choice == 4:
            lid = click.prompt("Enter Loan ID", type=int)
            field = click.prompt("Field to update (principle_amount, interest_rate, status)")
            value = click.prompt("New Value")
            update_loan(lid, **{field: value})
            click.secho("Loan updated successfully!", fg="green")

        elif loan_choice == 5:
            lid = click.prompt("Enter Loan ID", type=int)
            delete_loan(lid)
            click.secho("Loan deleted successfully!", fg="red")

    # ------------------ LOAN REPAYMENTS ------------------
    elif choice == 5:
        click.secho("\n--- Loan Repayments Menu ---", fg="blue")
        click.secho("1. Add Repayment", fg="yellow")
        click.secho("2. View All Repayments", fg="yellow")
        click.secho("3. View Repayment by ID", fg="yellow")
        click.secho("4. Update Repayment", fg="yellow")
        click.secho("5. Delete Repayment", fg="yellow")

        repay_choice = click.prompt("Select an option", type=int)

        if repay_choice == 1:
            lid = click.prompt("Loan ID", type=int)
            amt = click.prompt("Repayment Amount", type=float)
            date = click.prompt("Repayable Date (YYYY-MM-DD)")
            repay_date = datetime.strptime(date, "%Y-%m-%d")
            method = click.prompt("Method (cash/mpesa/bank)")
            add_loan_repayment(lid, amt, repay_date, method)
            click.secho("Repayment added successfully!", fg="green")

        elif repay_choice == 2:
            reps = get_all_repayments()
            for r in reps:
                click.secho(f"{r.id}: Loan={r.loan_id}, Amount={r.amount}, Date={r.repayable_date}, Method={r.method}", fg="cyan")

        elif repay_choice == 3:
            rid = click.prompt("Enter Repayment ID", type=int)
            r = get_repayment_by_id(rid)
            if r:
                click.secho(f"{r.id}: Loan={r.loan_id}, Amount={r.amount}, Date={r.repayable_date}, Method={r.method}", fg="cyan")
            else:
                click.secho("Repayment not found!", fg="red")

        elif repay_choice == 4:
            rid = click.prompt("Enter Repayment ID", type=int)
            field = click.prompt("Field to update (amount, repayable_date, method)")
            value = click.prompt("New Value")
            if field == "repayable_date":
                value = datetime.strptime(value, "%Y-%m-%d")
            update_repayment(rid, **{field: value})
            click.secho("Repayment updated successfully!", fg="green")

        elif repay_choice == 5:
            rid = click.prompt("Enter Repayment ID", type=int)
            delete_repayment(rid)
            click.secho("Repayment deleted successfully!", fg="red")

    elif choice == 6:
        click.secho("Goodbye 👋", fg="red")
        break
