import sqlite3
from mybudget.models import Transaction
from decimal import Decimal
from datetime import date

connection = sqlite3.connect("learning_budget.db")
connection.row_factory = sqlite3.Row

try: 
    cursor = connection.execute(
    """
    SELECT id, category, amount, transaction_date
    FROM transactions
    WHERE category = ?
    ORDER BY id
    """,
    ("Groceries",),
)
    rows = cursor.fetchall()

    transactions = []
    for row in rows:
        transactions.append(Transaction(row["category"], Decimal(row["amount"]), date.fromisoformat(row["transaction_date"])))
    print(transactions)
finally:
    connection.close()


