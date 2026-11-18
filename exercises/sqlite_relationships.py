import sqlite3

connection = sqlite3.connect(":memory:")
connection.execute("PRAGMA foreign_keys = ON")

connection.execute("""
    CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
    )
    """
    )

connection.execute("""
    CREATE TABLE transactions (
    id INTEGER PRIMARY KEY,
    category_id INTEGER NOT NULL,
    amount TEXT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
    )
    """
    )

connection.commit()

try:
    connection.execute(
    "INSERT INTO categories (name) VALUES (?)",
    ("Groceries",),
    )

    connection.commit()

    connection.execute(
        "INSERT INTO transactions (category_id, amount) VALUES (?, ?)",
        (1, "20.00"),
    )

    connection.commit()

    connection.execute(
        "INSERT INTO transactions (category_id, amount) VALUES (?, ?)",
        (999, "20.00"),
    )

    connection.commit()

except sqlite3.IntegrityError as error:
    connection.rollback()
    print(error)
   
finally:
    print(connection.execute(""" SELECT t.id, c.name, t.amount
FROM transactions AS t
INNER JOIN categories AS c
    ON t.category_id = c.id
ORDER BY t.id """).fetchall())
    connection.close()

