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
    """)
    connection.commit()
finally:
    connection.close()

