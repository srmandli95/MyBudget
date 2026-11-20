import sqlite3

first = sqlite3.connect("locking_learning.db")
second = sqlite3.connect("locking_learning.db", timeout=0)

first.execute(
    "UPDATE counters SET value = ? WHERE id = ?",
    (300, 1),
)
# The write transaction remains open because we haven't committed.

try:
    second.execute(
        "UPDATE counters SET value = ? WHERE id = ?",
        (500, 1),
    )
    second.commit()
except sqlite3.OperationalError as error:
    print("error: ", error)
finally:
    second.rollback()
    first.rollback()
    second.close()
    first.close()