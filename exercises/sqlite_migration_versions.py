import sqlite3 

connection = sqlite3.connect("migration_learning.db")


version = connection.execute("PRAGMA user_version").fetchone()[0]

if version == 0:
    connection.execute("BEGIN")
    try:
        connection.execute(
            "ALTER TABLE transactions ADD COLUMN merchant TEXT"
        )
        connection.execute("PRAGMA user_version = 1")
        connection.commit()
        print("Applied migration 1")
    except sqlite3.Error:
        connection.rollback()
        raise
else:
    print(f"Already at version {version}")

connection.close()