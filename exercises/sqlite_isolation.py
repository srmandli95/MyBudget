import sqlite3

setup = sqlite3.connect("isolation_learning.db")
try:
    setup.execute("""
        CREATE TABLE IF NOT EXISTS counters (
            id INTEGER PRIMARY KEY,
            value INTEGER NOT NULL
        )
    """)
    setup.execute("DELETE FROM counters")
    setup.execute("INSERT INTO counters (id, value) VALUES (?, ?)", (1, 100))
    setup.commit()
finally:
    setup.close()

first = sqlite3.connect("isolation_learning.db")
second = sqlite3.connect("isolation_learning.db")

print("before first commit")
first.execute(
    "UPDATE counters SET value = ? WHERE id = ?",
    (300, 1),
)

print(second.execute(
    """ Select * from counters """
).fetchall())

first.commit()

print("after first commit")
print(second.execute(
    """ Select * from counters """
).fetchall())


first.close()
second.close()