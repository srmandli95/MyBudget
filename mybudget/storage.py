import sqlite3
from mybudget.models import Transaction
from decimal import Decimal
from datetime import date

def initialize_database(connection: sqlite3.Connection) -> None:

    connection.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
            id INTEGER PRIMARY KEY,
            category TEXT NOT NULL CHECK(length(trim(category)) > 0),
            amount TEXT NOT NULL,
            transaction_date TEXT NOT NULL
        )
        """
    )



def save_transaction(
    connection: sqlite3.Connection,
    transaction: Transaction,
) -> None:

    connection.execute(
    """
    INSERT INTO transactions (category, amount, transaction_date)
    VALUES (?, ?, ?)
    """,
    (
        transaction.category,
        str(transaction.amount),
        transaction.transaction_date.isoformat(),
    ),
)

def load_transactions(
    connection: sqlite3.Connection,
) -> list[Transaction]:

    cursor = connection.execute(
        """
        SELECT id, category, amount, transaction_date
        FROM transactions
        ORDER BY id
        """
    )
    transactions = []
    for id, category, amount, transaction_date in cursor:
        transactions.append(Transaction(category, Decimal(amount), date.fromisoformat(transaction_date)))

    return transactions

