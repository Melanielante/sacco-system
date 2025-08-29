

# SACCO Management System

A simple **command-line application** for managing SACCO operations such as members, accounts, savings, loans, and repayments.
Built with **Python**, **SQLAlchemy ORM**, **Alembic**, and **Click**.

---

##  Features

* **Members Management**: Add, view, update, and delete SACCO members.
* **Accounts**: Manage member accounts.
* **Savings Transactions**: Record and view member savings.
* **Loans**: Issue and track loans.
* **Loan Repayments**: Record loan repayments.
* **Database Migrations** with **Alembic**.

---

##  Tech Stack

* **Python 3.8+**
* **SQLAlchemy ORM** – database modeling & queries
* **Alembic** – database migrations
* **Click** – command-line interface
* **Pipenv** – environment & dependency management

---

##  Project Structure

```bash
sacco-system/
│── sacco/
│   ├── __init__.py
│   ├── main.py          # CLI entry point
│   ├── crud.py          # CRUD operations
│   ├── models.py        # Database models
│   ├── relationships.py # Model relationships
│   ├── db.py            # Database connection setup
│── alembic/             # Alembic migration files
│── alembic.ini          # Alembic config
│── Pipfile              # Pipenv dependencies
│── Pipfile.lock
│── README.md            # Project documentation
```

---

##  Installation & Setup

### 1. Clone the Repository

```bash
git clone git@github.com:Melanielante/sacco-system.git
cd sacco-system
```

### 2. Create & Activate Virtual Environment (Pipenv)

```bash
pipenv install --dev
pipenv shell
```

### 3. Run Database Migrations

```bash
alembic upgrade head
```

### 4. Start the Application

```bash
python -m sacco.main
```

---

##  Database Management

### Run a New Migration

```bash
alembic revision --autogenerate -m "description of changes"
```

### Apply Migrations

```bash
alembic upgrade head
```

### Rollback Last Migration

```bash
alembic downgrade -1
```

---

##  Usage

When you run the app:

```bash
====== SACCO SYSTEM ======
1. Members
2. Accounts
3. Savings Transactions
4. Loans
5. Loan Repayments
6. Exit
```

Example:

* Select `1` → Manage members
* Add, view, update, or delete members

---

##  To-Do / Future Improvements

* Add authentication for admin and members
* Improve error handling
* Add reporting & analytics (savings, loans, repayments)
* REST API with FastAPI/Flask

---

##  Contributing

1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Push to your branch
5. Open a Pull Request

---

##  License

This project is licensed under the **MIT License**.

