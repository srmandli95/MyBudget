import sqlite3

connection = sqlite3.connect(":memory:")

try:
    connection.execute("""
        CREATE TABLE transactions (
            id INTEGER PRIMARY KEY,
            category TEXT NOT NULL
        )
    """)

    query = """
        EXPLAIN QUERY PLAN
        SELECT id, category
        FROM transactions
        WHERE category = ?
    """

    print("Before:", connection.execute(query, ("Groceries",)).fetchall())

    connection.execute(
        "CREATE INDEX idx_transactions_category ON transactions(category)"
    )

    print("After:", connection.execute(query, ("Groceries",)).fetchall())
finally:
    connection.close()