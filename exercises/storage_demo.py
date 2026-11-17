import sqlite3
from mybudget.storage import initialize_database, save_transaction
from mybudget.models import Transaction
from decimal import Decimal
from datetime import date

connection = sqlite3.connect(":memory:")

t1 = Transaction("Groceries", Decimal("22.45"), date(2026,10,10))

try:
    initialize_database(connection)
    connection.commit()
    save_transaction(connection, t1)
    connection.commit()
    print(connection.execute(
    "SELECT category, amount, transaction_date FROM transactions"
).fetchall())
except sqlite3.Error:
    connection.rollback()
    raise

finally:
    connection.close()

