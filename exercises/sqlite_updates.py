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


connection.execute(
    "INSERT INTO transactions (category, amount) VALUES (?, ?)",
    ("Groceries", "40.00"),
    )

connection.execute(
        "INSERT INTO transactions (category, amount) VALUES (?, ?)",
        ("gas", "20.00"),
    )

connection.commit()

try:
    connection.execute(
        "UPDATE transactions SET amount = ? where id = ?",
        ("55.00", 1),
    )

    connection.commit()

    connection.execute(
    "DELETE FROM transactions WHERE id = ?",
    (2,),
    )
    connection.commit()

finally:
    print(connection.execute("SELECT id, category, amount FROM transactions ORDER BY id").fetchall())
    connection.close()