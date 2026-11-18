import sqlite3
from decimal import Decimal
connection = sqlite3.connect(":memory:")

try:
    connection.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            amount_cents INTEGER NOT NULL
        )
        """
        )

    connection.commit()

    cursor = connection.execute(""" SELECT COALESCE(SUM(amount_cents), 0) FROM transactions """)
    total_cents = cursor.fetchone()[0]
    total_amount = Decimal(total_cents) / 100
    print(f"{total_amount:.2f}")

    connection.execute(
            "INSERT INTO transactions (amount_cents) VALUES (?)",
            (2000,),
        )

    connection.commit()

    connection.execute(
            "INSERT INTO transactions (amount_cents) VALUES (?)",
            (2500,),
        )

    connection.commit()

    cursor = connection.execute(
    "SELECT SUM(amount_cents) FROM transactions"
    )   
    total_cents = cursor.fetchone()[0]
    total_amount = Decimal(total_cents) / 100
    print(f"{total_amount:.2f}")

except sqlite3.IntegrityError as error:
    print(error)

finally:

   
    connection.close()

