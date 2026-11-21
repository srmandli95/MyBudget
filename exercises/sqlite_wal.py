import sqlite3

setup = sqlite3.connect("wal_learning.db")
try:
    setup.execute("PRAGMA journal_mode = WAL")
    setup.execute("""
        CREATE TABLE IF NOT EXISTS counters (
            id INTEGER PRIMARY KEY,
            value INTEGER NOT NULL
        )
    """)
    setup.execute("DELETE FROM counters")
    setup.execute(
        "INSERT INTO counters (id, value) VALUES (?, ?)",
        (1, 100),
    )
    setup.commit()
finally:
    setup.close()


reader = sqlite3.connect("wal_learning.db")
writer = sqlite3.connect("wal_learning.db")

reader.execute("BEGIN")

print(reader.execute(
    "SELECT value FROM counters WHERE id = ?", (1,)
).fetchone()[0])

writer.execute(
        "UPDATE counters SET value = ? where id = ?",
        (300, 1),
    )

writer.commit()

print(reader.execute(
    "SELECT value FROM counters WHERE id = ?", (1,)
).fetchone()[0])

reader.commit()

print(reader.execute(
    "SELECT value FROM counters WHERE id = ?", (1,)
).fetchone()[0])
