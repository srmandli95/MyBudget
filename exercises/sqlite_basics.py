import sqlite3

connection = sqlite3.connect("learning_budget.db")

try:
    connection.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        category TEXT NOT NULL,
        amount TEXT NOT NULL,
        transaction_date TEXT NOT NULL
       )
    """
    )

    connection.execute(
        """
        INSERT INTO transactions ( category, amount, transaction_date)
        VALUES (?, ?, ?)
        """,
        ("Groceries", "40.00", "2026-11-14"),
    )
    connection.commit()

    cursor = connection.execute(
        "SELECT id, category, amount, transaction_date FROM transactions"
    )
    rows = cursor.fetchall()

    for row in rows:
        print(row)
finally:
    connection.close()

