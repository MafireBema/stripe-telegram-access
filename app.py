from webhook import app

if __name__ == "__main__":
    app.run()
import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY
        )
    ''')
    conn.commit()
    conn.close()

init_db()
