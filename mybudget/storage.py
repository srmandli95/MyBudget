import sqlite3
from mybudget.models import Transaction

def initialize_database(connection: sqlite3.Connection) -> None:

    connection.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
            id INTEGER PRIMARY KEY,
            category TEXT NOT NULL,
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

