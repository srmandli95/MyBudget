import sqlite3

connection = sqlite3.connect(":memory:")

connection.execute("""
        CREATE TABLE transactions (
    id INTEGER PRIMARY KEY,
    category TEXT NOT NULL,
    amount_cents INTEGER NOT NULL
)
    """)

connection.commit()

connection.execute(
        """
        INSERT INTO transactions (category, amount_cents)
        VALUES (?, ?)
        """,
        ("Groceries", 2000),
    )

connection.commit()

connection.execute("""
ALTER TABLE transactions ADD COLUMN merchant TEXT
""")

connection.commit()

print(connection.execute("""
SELECT id, category, amount_cents, merchant FROM transactions
""").fetchall())


connection.execute(
    "UPDATE transactions SET merchant = ? WHERE id = ?",
    ("Costco", 1),
)
connection.commit()

print(connection.execute("""
SELECT id, category, amount_cents, merchant FROM transactions
""").fetchall())


connection.close()