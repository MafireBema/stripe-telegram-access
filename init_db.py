import sqlite3

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE
    )
''')

conn.commit()
conn.close()

print("✅ Datenbank erstellt: users.db")
