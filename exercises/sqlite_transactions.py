import sqlite3

connection = sqlite3.connect(":memory:")

connection.execute("""
    CREATE TABLE IF NOT EXISTS transactions(
        id INTEGER PRIMARY KEY,
        category TEXT NOT NULL,
        amount TEXT NOT NULL
    )
    """
    )

try:
    connection.execute(
    "INSERT INTO transactions (category, amount) VALUES (?, ?)",
    ("Groceries", "40.00"),
    )

    connection.execute(
        "INSERT INTO transactions (category, amount) VALUES (?, ?)",
        (None, "20.00"),
    )

    connection.commit()

except sqlite3.IntegrityError:
    connection.rollback()
   
finally:
    print(connection.execute("SELECT * FROM transactions").fetchall())
    connection.close()



