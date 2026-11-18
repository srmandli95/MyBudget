import sqlite3

connection = sqlite3.connect(":memory:")

connection.execute("""
        CREATE TABLE transactions (
            id INTEGER PRIMARY KEY,
            category TEXT NOT NULL,
            transaction_date TEXT
        )
    """)

connection.execute("""
        CREATE INDEX idx_category_date
        ON transactions(category, transaction_date);
    """)

query = """
        EXPLAIN QUERY PLAN
        SELECT id FROM transactions
WHERE category = ? AND transaction_date >= ?
    """

print(connection.execute(query, ("Groceries", "2026-11-01")).fetchall())


    