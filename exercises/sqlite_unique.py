import sqlite3

connection = sqlite3.connect(":memory:")

connection.execute("""
    CREATE TABLE category (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
    """
    )

connection.commit()

try:
    connection.execute(
    "INSERT INTO category (name) VALUES (?)",
    ("Groceries",),
    )
    connection.commit()
    connection.execute(
    "INSERT INTO category (name) VALUES (?)",
    ("Groceries",),
    )
    connection.commit()
except sqlite3.IntegrityError as error:
    connection.rollback()
    print(error)

finally:
    print(connection.execute("SELECT id, name FROM category").fetchall())
    connection.close()

