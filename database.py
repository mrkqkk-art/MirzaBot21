import sqlite3

DB = "users.db"


def connect():
    return sqlite3.connect(DB)


def create_db():
    con = connect()
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT
    )
    """)

    con.commit()
    con.close()


def add_user(user_id, username):
    con = connect()
    cur = con.cursor()

    cur.execute(
        "INSERT OR IGNORE INTO users VALUES (?,?)",
        (user_id, username)
    )

    con.commit()
    con.close()


def users_count():
    con = connect()
    cur = con.cursor()

    cur.execute("SELECT COUNT(*) FROM users")
    count = cur.fetchone()[0]

    con.close()
    return count
